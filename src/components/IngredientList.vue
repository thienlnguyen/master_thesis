<template>
  <div>
    <span class="heading">{{ title }}</span>
    <div class="ingredient-container" v-show="ingredients">
      <div
        class="ingredient"
        v-for="(item, index) in ingredients"
        :key="item.id"
      >
        <hr v-if="index > 0" class="line" />
        <div class="grid-container col-2">
          <div class="grid-item align-left">
            <span class="label">{{ item.name }}</span>
          </div>
          <div class="grid-container button-container">
            <div class="grid-btn" @click="$emit('editIngredient', item)">
              <font-awesome-icon
                class="btn-edit"
                :icon="['far', 'pen-to-square']"
              />
            </div>
            <div class="grid-btn" @click="$emit('trigger-popup', item)">
              <font-awesome-icon class="btn-remove" icon="xmark" />
            </div>
          </div>
        </div>
        <div class="grid-container col-3">
          <div class="grid-item align-left">
            <span>{{ item.gram }}g</span>
          </div>
          <div class="grid-item align-center">
            <span>{{ item.nutritions.kcal }}kcal</span>
          </div>
        </div>
        <div class="grid-container col-3">
          <div class="grid-item align-left">
            <span>carbs: {{ item.nutritions.carbs }}g</span>
          </div>
          <div class="grid-item align-center">
            <span>protein: {{ item.nutritions.protein }}g</span>
          </div>
          <div class="grid-item align-right">
            <span>fat: {{ item.nutritions.fat }}g</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

  <script>
export default {
  name: "IngredientList",
  props: {
    title: {
      type: String,
      default: "ingredients",
    },
    ingredients: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped>
.heading {
  font-size: 12px;
  color: #888888;
  font-weight: bold;
  margin-bottom: 1rem;
}
.grid-container {
  width: 100%;
  display: grid;
  gap: 10px;
}
.col-2{
  grid-template-columns: 1fr 1fr;
}
.col-3{
  grid-template-columns: 1fr 1fr 1fr;
}
.grid-item {
  display: flex;
  justify-content: center;
  flex-direction: column;
  font-size: 12px;
  margin: 5px 0;
}
.ingredient-container {
  border: 1px solid #cecece;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1rem;
  color: #888888;
}
.line {
  width: 100%;
  margin: 8px 0;
  border: 0.5px solid #cecece;
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
  color: #6d91cd;
}
.btn-remove {
  height: 28px;
  color: #fa8585;
}
.label {
  font-weight: bold;
}
</style>
