from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import numpy as np
import os
from PIL import Image
import torch
import torchvision.transforms as transforms
import json
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")


app = Flask(__name__, static_folder="dist", static_url_path="")

CORS(app)

try:
    client = MongoClient(MONGO_URI, tls=True,
    tlsAllowInvalidCertificates=True)
    foodDB = client.foodDB
    diaryDB = client.diaryDB
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(f"Error while connecting to MongoDB: {e}")

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODEL_PATH = './model/resnet50_complete.pth'
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = torch.load(MODEL_PATH, map_location='cpu')
model.eval()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

with open('data/class_names.json', 'r') as f:
    food101_classes = json.load(f)

def get_food(pred_class):
    food = foodDB.food101.find_one({"name": pred_class})
    return food

@app.route("/")
def serve_index():
    return send_from_directory("dist", "index.html")

@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory("dist", path)

@app.route("/api/upload", methods=['POST'], strict_slashes=False)
def upload_file():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            return jsonify({'error': 'Unsupported file format'}), 400

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            print("Öffne und transformiere das Bild...")
            img = Image.open(filepath).convert('RGB')
            img_tensor = transform(img).unsqueeze(0).to(device)
        except Exception as img_err:
            print(f"Bildverarbeitungsfehler: {img_err}")
            return jsonify({'error': f'Error processing the image: {str(img_err)}'}), 500

        with torch.no_grad():
            output = model(img_tensor)

        predicted_idx = torch.argmax(output, dim=1).item()

        if predicted_idx < len(food101_classes):
            pred_class = food101_classes[predicted_idx]
        else:
            pred_class = f"Unknown class index {predicted_idx}"

        try:
            food = get_food(pred_class)
            print(f"Ergebnis aus get_food(): {food}")
        except Exception as food_err:
            print(f"Fehler bei get_food(): {food_err}")
            return jsonify({'error': f'Error getting food: {str(food_err)}'}), 500

        food_id = str(food["id"]) if food and "id" in food else "Not found"

        return jsonify({
            'filepath': os.path.basename(filepath),
            'predicted_class': pred_class,
            'id': food_id,
        }), 200

    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return jsonify({'error': str(e)}), 500


@app.route("/api/getIngredients", methods=['POST'], strict_slashes=False)
def get_ingredients():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': 'Invalid JSON or No JSON data provided'}), 400

    requested_id = int(data.get('id'))

    food = foodDB.food101.find_one({"id": requested_id})
    food["_id"] = str(food["_id"])
    ingredients = food["ingredients"]
    print(ingredients)
    ingredients_nutri = []

    for ing in ingredients.split(", "):
        ingredient_data = foodDB.ingredients.find_one({"name": ing})

        if ingredient_data:
            ingredient_data["_id"] = str(ingredient_data["_id"]) if "_id" in ingredient_data else None
            ingredients_nutri.append(ingredient_data)

    return jsonify({
        'food_name': food["name"],
        'ingredients': ingredients_nutri
    }), 200


@app.route("/api/addMeal", methods=['POST'], strict_slashes=False)
def add_meal():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Invalid JSON or No JSON data provided'}), 400

    new_entry = {
        "date": str(data["date"]),
        data["typeOfMeal"]: data["ingredients"]
    }

    find_entry = diaryDB.diary.find_one({"date": str(data["date"])})

    if find_entry:
        update_result = diaryDB.diary.update_one(
            {"date": str(data["date"])},
            {"$set": {data["typeOfMeal"]: data["ingredients"]}}
        )

        return jsonify({
            'message': "Updated existing entry",
            'matched_count': update_result.matched_count,
            'modified_count': update_result.modified_count
        }), 200
    else:
        inserted = diaryDB.diary.insert_one(new_entry)

        return jsonify({
            'message': "Inserted new entry",
            'inserted_id': str(inserted.inserted_id)
        }), 201

@app.route("/api/getEntries/<date>", methods=['GET'], strict_slashes=False)
def get_entries(date):
    find_entry = diaryDB.diary.find_one({"date": str(date)})

    print(date)
    print(find_entry)
    if not find_entry:
        return jsonify({"error": "No entry found for this date"}), 404

    find_entry["_id"] = str(find_entry["_id"])

    return jsonify({"entry": find_entry}), 200

@app.route("/api/getIngredient/<query>", methods=['GET'], strict_slashes=False)
def get_ingredient(query):
    find_entry = foodDB.ingredients.find_one({"name": str(query)})

    print(find_entry)
    if not find_entry:
        return jsonify({"error": "No entry found for this date"}), 404

    find_entry["_id"] = str(find_entry["_id"])

    return jsonify({"ingredient": find_entry}), 200

@app.errorhandler(404)
def not_found(e):
    return send_from_directory("dist", "index.html")

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host="0.0.0.0", port=5000, debug=True)