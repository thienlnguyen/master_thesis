<template>
    <div>
        <span class="heading">{{ title }}</span>
        <div class="foodlogs-detail">
            <div v-for="(item, index) in foodLogs" :key="item.meal">
                <hr v-if="index>0" class="line"/>
                <div class="grid-container" >
                    <div class="grid-item label" @click="seeDetails(item.meal)">
                        {{ item.meal }}
                    </div>
                    <div class="grid-item value" @click="seeDetails(item.meal)">
                        {{ item.totalCals }} / {{ item.calcIntake }}
                    </div>
                    <div class="grid-item btn">
                      <ImageUpload class="add-btn" id="item.meal" :typeOfMeal="item.meal"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

  <script>
  import ImageUpload from './ImageUpload.vue';
  export default {
    name: "FoodLogs",
    components: {
      ImageUpload
    },
    props: {
      title: {
        type: String,
        default: "food logs"
      },
      foodLogs: {
        type: Array,
        required: true
      }
    },
    methods:{
      seeDetails(meal){
        this.$router.push({
        name: "seeDetails",
        params: {
          typeOfMeal: encodeURIComponent(meal)
        }
      });
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
.foodlogs-detail {
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
  grid-template-columns: 33%;
}
.grid-item {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.label {
  font-weight: bold;
  color: #888888;
  font-size: 12px;
  align-items: start;
}
.value {
  color: #888888;
  font-size: 12px;
  text-align: center;
  font-weight: bold;
  text-align: center;
}
.btn{
  align-items: end;
}
.add-btn{
  height: 35px;
  width: 35px;
}
.line{
  width: 100%;
  margin: 8px 0;
  border: 0.5px solid #CECECE;
}
.imageInput{
  display: none;
}
  </style>
