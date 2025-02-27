<template>
<div>
  <div  v-if="!showEdit && !showSearch">
    <div>
      <img class="image-preview" :src="'/uploads/'+$route.params.imageUrl" alt="Selected Image" />
    </div>
    <div class="nutrition-sum grid-container column-4">
      <div class="grid-item align-center" v-for="nutri in sumNutritions" :key="nutri.name">
        <span class="nutri-value">{{ nutri.value }}</span>
        <span class="nutri-name">{{ nutri.name }}</span>
      </div>
    </div>
    <IngredientList :ingredients="ingredients" @editIngredient="editIngredient" @trigger-popup="showRemovePopup" />
    <div class="buttons-container">
      <button class="btn-item add-ingredient" @click="addingredient">add ingredient</button>
      <button class="btn-item add-meal" @click="addMeal">add meal to diary</button>
    </div>
  </div>
  <PopupDialog
      v-if="showPopup"
      :title="popupTitle"
      :message="popupMessage"
      :submitLabel="popupSubmitLabel"
      :isVisible="showPopup"
      :itemId="selectedItemId"
      @confirm="handleConfirm"
      @cancel="showPopup = false"
    />
  <EditIngredient
      v-if="showEdit"
      :ingredient="selectedItemId"
      @save="saveEdits"
      @cancel="showEdit = false"
    />
    <SearchIngredient
    v-if="selectedDate"
     @editIngredient="editIngredient"
    />
</div>
</template>

<script>
import IngredientList from "@/components/IngredientList.vue"
import PopupDialog from "@/components/PopupDialog.vue"
import EditIngredient from "@/components/EditIngredient.vue"
import SearchIngredient from "@/components/SearchIngredient.vue"

export default {
  name: "AddMealView",
  data() {
    return {
      ingredients: [],
      showPopup: false,
      showSearch: false,
      showEdit: false,
      popupTitle: "",
      popupMessage: "",
      popupSubmitLabel: "",
      selectedItemId: null,
    };
  },
  props: ["selectedDate"],
  components: {
    IngredientList,
    PopupDialog,
    EditIngredient,
    SearchIngredient,
  },
  computed: {
    sumNutritions() {
      const nutrients = ["kcal", "carbs", "protein", "fat"];
      const totalNutrients = nutrients.map(nutri => ({
        name: nutri,
        value: this.ingredients.reduce((sum, food) => {
          return sum + (food.nutritions?.[nutri] || 0);
        }, 0)
      }));

      return totalNutrients;
    }
  },
  mounted() {
    fetch("/api/getIngredients", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        id: this.$route.params.id
      })
    })
    .then(response => response.json())
    .then(data => {
      this.ingredients = data.ingredients;
    })
  },
  methods:{
    showRemovePopup(item) {
      this.selectedItemId = item.id;
      this.popupTitle = `${item.name} entfernen?`;
      this.popupMessage = "Möchtest du dieses Element wirklich löschen?";
      this.popupSubmitLabel = "Löschen";
      this.showPopup = true;
    },
    handleConfirm(id) {
      console.log(`${this.selectedItemId} wird gelöscht!`);
      this.ingredients = this.ingredients.filter((obj) => obj.id !== id);
      this.showPopup = false;
    },
    editIngredient(item){
    this.selectedItemId = item;
    this.showEdit = true;
    },
    saveEdits(item){
      if (this.ingredients.length === 0) {
        this.ingredients.push(item);
      } else {
        this.ingredients = this.ingredients.map(obj =>
          obj.id === item.id ? item : obj
        );
        if (!this.ingredients.some(obj => obj.id === item.id)) {
          this.ingredients.push(item);
        }
      }
      this.showEdit = false;
    },
    addIngredientToMeal(newIngredient) {
    this.ingredients.push(newIngredient);
    this.addMeal()
    },
    addMeal(){
      fetch("/api/addMeal", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        typeOfMeal: this.$route.params.typeOfMeal,
        ingredients: this.ingredients,
        date: this.selectedDate,
      })
    })
    .then(response => response.json())
    .then(data => {
      this.$router.push({
        path: "/",
      });
    })
    }
  }
};

</script>

<style scoped>
.image-preview {
  max-height: 470px;
  overflow: hidden;
  border-radius: 15px;
  width: 100%;
}
.image-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 15px;
  object-position: center;
}
.heading {
  font-size: 12px;
  color: #888888;
  font-weight: bold;
  margin-bottom:1rem;
}
.grid-container {
  width: 100%;
  display: grid;
  gap: 10px;
}
.column-3 {
  grid-template-columns: 1fr 1fr 1fr;

}
.column-4 {
  grid-template-columns: 1fr 1fr 1fr 1fr;
}
.grid-item {
  display: flex;
  justify-content: center;
  flex-direction: column;
  font-size: 12px;
  margin: 5px 0;
}
.ingredient-container {
  border: 1px solid #CECECE;
 border-radius: 15px;
  padding: 1rem;
  margin-bottom: 1rem;
  color: #888888;
}
.line {
  width: 100%;
  margin: 8px 0;
  border: 0.5px solid #CECECE;
}
.align-left {
  align-items: start;
}
.align-center {
  align-items: center;
}
.align-right {
  align-items: end;
}
.grid-container.button-container {
  justify-content: flex-end;
  display: flex;
  gap: 20px;
}
.btn-edit {
  height: 23px;
  color: #6D91CD;
}
.btn-remove {
  height: 28px;
  color: #fa8585;
}
.label{
  font-weight:bold;
}
.nutrition-sum{
  background-color: #d9d9d9;
  color: white;
 border-radius: 15px;
  padding: 5px;
  margin: 1rem 0;
}
.nutri-value{
  font-size: 14px;
  font-weight: bold;
}
.nutri-name{
  font-size: 12px;
  font-weight: bold;
}
.btn-item{
  width:80%;
  height: 40px;
  color: white;
  border-radius: 50px;
  border: none;
  margin: 0 auto 15px auto;
  align-items: center;
  display: flex;
  justify-content: center;
  font-weight: bold;
  font-size: 14px;
}
.btn-item.add-ingredient{
  background-color: #6D91CD;
}
.btn-item.add-meal{
  background-color: #AAC0E6;
}
</style>
