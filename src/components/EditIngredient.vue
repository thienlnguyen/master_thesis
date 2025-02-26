<template>
  <div>
    <div class="heading-container">
      <span class="heading">{{ title }}</span>
    </div>
    <div class="grid-container">
      <div class="grid-item">
        <input v-model.number="roundedValue" type="number" class="gram" min="0" @change="adjustNutrients"/> g
      </div>
      <div class="grid-item">
        <span>{{ updatedIngredient.name }}</span>
      </div>
    </div>
    <button class="btn-item" @click="save">save ingredient</button>
  </div>
</template>

<script>
export default {
  name: "EditIngredient",
  data() {
    return {
      newValue: this.ingredient.gram,
      updatedIngredient: { ...this.ingredient },
    };
  },
  computed: {
    roundedValue: {
      get() {
        return Math.round(this.newValue);
      },
      set(value) {
        this.newValue = Math.round(value);
      }
    }
  },
  props: {
    title: {
      type: String,
      default: "edit ingredient",
    },
    diaryId: {
      type: String
    },
    ingredient: {
      type: Object,
      required: true,
    },
  },
  emits: ["save", "cancel", "update:ingredient"],
  methods: {
    save() {
      this.$emit("save", this.updatedIngredient);
      this.$emit("update:ingredient", this.updatedIngredient);
    },
    cancel() {
      this.$emit("cancel");
    },
    adjustNutrients() {
      if (this.newValue < 0) {
        this.newValue = 0;
      }
      if (this.updatedIngredient.gram > 0 && this.newValue > 0) {
        const scaleFactor = this.newValue / this.updatedIngredient.gram;
        this.updatedIngredient = {
          ...this.updatedIngredient,
          nutritions: {
            kcal: Math.round(this.updatedIngredient.nutritions.kcal * scaleFactor),
            carbs: Math.round(this.updatedIngredient.nutritions.carbs * scaleFactor),
            fat: Math.round(this.updatedIngredient.nutritions.fat * scaleFactor),
            protein: Math.round(this.updatedIngredient.nutritions.protein * scaleFactor),
          },
          gram: Math.round(this.newValue),
        };
        this.$emit("update:ingredient", { ...this.updatedIngredient });
      }
    }
  },
  watch: {
    ingredient: {
      handler(newValue) {
        this.updatedIngredient = { ...newValue };
        this.newValue = Math.round(newValue.gram);
      },
      deep: true,
      immediate: true
    }
  }
}
</script>

<style scoped>
.heading-container{
  text-align: center;
}
.heading {
  font-size: 12px;
  color: #888888;
  font-weight: bold;
  margin-bottom: 1rem;
}
.gram{
  width: 40%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 15px;
}
.btn-item {
  width: 80%;
  height: 40px;
  color: white;
  border-radius: 50px;
  border: none;
  margin: 10px auto;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 14px;
  background-color: #6D91CD;
}
.grid-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
}
.grid-item {
  display: flex;
  align-items: center;
  gap: 5px;
}
</style>
