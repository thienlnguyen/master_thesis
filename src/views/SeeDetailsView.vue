<template>
  <div>
    <div v-if="!showEdit && !showSearch">
      <IngredientList
        :ingredients="ingredients"
        @trigger-popup="showRemovePopup"
        @editIngredient="editIngredient"
      />
      <div class="buttons-container">
        <button class="btn-item add-ingredient" @click="addIngredient">add ingredient</button>
        <button
          v-if="isModified"
          class="btn-item add-meal"
          @click="save()">
          save changes
        </button>
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
      v-if="showEdit && !showSearch"
      :ingredient="selectedItemId"
      @save="saveEdits"
      @cancel="showEdit = false"
    />
    <SearchIngredient v-show="showSearch && !showEdit"
    @editIngredient="editIngredient"
    />
  </div>
</template>

<script>
import IngredientList from "@/components/IngredientList.vue";
import PopupDialog from "@/components/PopupDialog.vue";
import EditIngredient from "@/components/EditIngredient.vue";
import SearchIngredient from "@/components/SearchIngredient.vue";


export default {
  name: "SeeDetails",
  props: ["selectedDate"],
  components: {
    IngredientList,
    PopupDialog,
    EditIngredient,
    SearchIngredient,
  },
  data() {
    return {
      ingredients: [],
      showPopup: false,
      showEdit: false,
      showSearch: false,
      popupTitle: "",
      popupMessage: "",
      popupSubmitLabel: "",
      selectedItemId: null,
      isModified: false,
    };
  },
  mounted() {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/getEntries/${this.selectedDate}`, { method: "GET" })
      .then((response) => response.json())
      .then((data) => {
        this.ingredients = data.entry[this.$route.params.typeOfMeal] || [];
      })
      .catch((error) => {
        console.error("Fehler beim Abrufen der Daten:", error);
      });
  },
  methods: {
    addIngredient() {
      this.showSearch =true
    },
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
      this.isModified = true;
      this.showPopup = false;
    },
    editIngredient(item){
      this.selectedItemId = item;
      this.showEdit = true;
      this.showSearch = false;
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
      this.showSearch = false;
      this.isModified = true;
    },
    save() {
      fetch(`${import.meta.env.VITE_API_BASE_URL}/addMeal`, {
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
      });
    },
  },
};
</script>

<style scoped>
/* Dein vorhandenes Styling */
.buttons-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.btn-item {
  width: 80%;
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
.btn-item.add-ingredient {
  background-color: #6D91CD;
}
.btn-item.add-meal {
  background-color: #AAC0E6;
}
</style>
