<template>
  <div>
    <span class="heading">{{ title }}</span>
    <div class="calories-detail">
      <div class="grid-container">
        <div class="grid-item" v-for="(item, index) in caloriesData" :key="index">
          <div class="value">
            {{ item.kcal }}
          </div>
          <div class="label">
            {{ item.label }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

  <script>
  export default {
    name: "CalorieDashboard",
    props: {
      title: {
        type: String,
        default: "calories"
      },
      caloriesData: {
        type: Array,
        required: true
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
  .calories-detail {
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
    font-size: 14px;
    text-align: center;
    font-weight: bold;
  }
  </style>
