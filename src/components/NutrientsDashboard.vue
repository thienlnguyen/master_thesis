<template>
    <div>
      <span class="heading">{{ title }}</span>
      <div class="nutrient-detail">
        <div class="grid-container">
          <div class="grid-item" v-for="item in nutrientsData" :key="item.nutrient">
            <div class="label" >
              {{ item.nutrient }}
            </div>
            <div class="progress-bar">
              <div class="progress" :style="{ width: Math.min(item.percentage, 100) + '%' }"></div>
            </div>
            <div class="value">
            {{ item.total }} / {{ item.intake }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>

  <script>
  export default {
    name: "NutrientsDashboard",
    props: {
      title: {
        type: String,
        default: "nutrients"
      },
      nutrientsData: {
        type: Array,
        required: true,
      }
    }
  };
  </script>

  <style scoped>
  .heading {
    font-size: 12px;
    color: #888888;
    font-weight: bold;
  }
  .nutrient-detail {
    border: 1px solid #CECECE;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
  }
  .grid-container {
    width: 100%;
    display: inline-grid;
    grid-auto-flow: column;
    gap: 10px;
  }
  .grid-item {
    align-items: center;
    display: flex;
    justify-content: center;
    text-align: center;
    flex-direction: column;
  }
  .label {
    font-weight: bold;
    color: #888888;
    font-size: 12px;
    text-align: center;
  }
  .value {
    color: #888888;
    font-size: 12px;
    text-align: center;
    font-weight: bold;
  }
  .progress-bar {
    background-color: #D9D9D9;
    height: 7px;
    width: 85px;
    border-radius: 3px;
    font-weight: bold;
    margin: 5px 0;
  }
  .progress {
    background-color: #6D91CD;
    height: 7px;
    border-radius: 3px;
  }
  </style>
