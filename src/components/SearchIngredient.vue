<template>
  <div>
    <div>
      <div class="heading"> search ingredient</div>
        <div class="grid-container">
        <input v-model="searchQuery" type="text" placeholder="ingredient" class="grid-item search-input" />
        <button @click="addIngredient" class="grid-item search-btn">
            <font-awesome-icon class="btn-plus" icon="plus" />
        </button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "SearchIngredient",
  data() {
    return {
      searchQuery: "",
    };
  },
  methods: {
    addIngredient() {
      fetch(`/api/getIngredient/${this.searchQuery}`, { method: "GET" })
        .then((response) => response.json())
        .then((data) => {
          if (data.ingredient) {
            this.$emit("editIngredient", data.ingredient);
          }
      })
      .catch((error) => {
        console.error("Fehler beim Abrufen der Daten:", error);
      });
      this.searchQuery = "";
    },
  }
}
</script>
<style>
.heading {
  font-size: 12px;
  color: #888888;
  align-items: center;
  font-weight: bold;
}
.search-input{
  height: 35px;
  width: 100%;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
  border: 1px solid #CECECE;
  padding: 1rem;
  font-size: 12px;
  margin-bottom: 1rem;
}
.search-btn{
  height: 35px;
  border-top-right-radius: 15px;
  border-bottom-right-radius: 15px;
  border: none;
  background-color: #6D91CD;
}
.grid-container {
  width: 100%;
  display: inline-grid;
  grid-auto-flow: column;
}
.grid-item {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.add-btn {
  border-radius: 50%;
  background-color: white;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;

}
.btn-plus {
  color: white;
  height: 20px;
}
</style>
