<template>
  <div>
    <CalorieDashboard :caloriesData="sumCals" />
    <NutrientsDashboard :nutrientsData="sumNutrients" />
    <FoodLogs :foodLogs="sumFoodLogs" />
  </div>
</template>

<script>
import NutrientsDashboard from "@/components/NutrientsDashboard.vue";
import CalorieDashboard from "@/components/CalorieDashboard.vue";
import FoodLogs from "@/components/FoodLogs.vue";
import data from "../../data/data.json";

export default {
  name: "DiaryView",
  components: {
    NutrientsDashboard,
    CalorieDashboard,
    FoodLogs
  },
  props: ["selectedDate"],
  data() {
    return {
      output: data.user.output,
      foodLogs: {
        breakfast: [],
        lunch: [],
        dinner: [],
        snack: []
      },
      activity: [],
      steps: { kcal: 0 }
    };
  },
  computed: {
    allMeals() {
      return [
        ...(this.foodLogs.breakfast || []),
        ...(this.foodLogs.lunch || []),
        ...(this.foodLogs.dinner || []),
        ...(this.foodLogs.snack || [])
      ];
    },
    intake() {
      return {
        kcal: this.output.macronutrients.kcal,
        carbs: this.output.macronutrients.carbs,
        protein: this.output.macronutrients.protein,
        fat: this.output.macronutrients.fat
      };
    },
    sumNutrients() {
      const nutrients = ["carbs", "protein", "fat"];
      return nutrients.map((nutrient) => {
        const total = Math.round(
          this.allMeals.reduce((sum, food) => sum + (food.nutritions?.[nutrient] || 0), 0)
        );
        const intake = this.intake[nutrient] || 1;
        const percentage = Math.round((total / intake) * 100);

        return {
          nutrient,
          total,
          intake,
          percentage
        };
      });
    },
    sumActivities() {
      const activities = ["duration", "kcal"];
      return activities.map((activity) => {
        const total = (this.activity || []).reduce(
          (sum, sport) => sum + (sport[activity] || 0),
          0
        );
        return {
          activity,
          total
        };
      });
    },
    sumCals() {
      const eaten = this.allMeals.reduce((sum, food) => sum + (food.nutritions?.kcal || 0), 0) || 0;
      const goal = this.output.calorieIntake || 0;
      const remaining = Math.max(goal - eaten, 0);
      const activities = this.sumActivities || [];
      const burned = (activities.find((act) => act.activity === "kcal")?.total || 0) + (this.steps?.kcal || 0);
      const over = eaten > goal ? eaten - goal : 0;

      return [
        { label: "remaining", kcal: remaining },
        { label: "over", kcal: over },
        { label: "goal", kcal: goal },
        { label: "eaten", kcal: eaten },
        { label: "burned", kcal: burned }
      ];
    },
    sumFoodLogs() {
      const meals = ["breakfast", "lunch", "dinner", "snack"];
      return meals.map((meal) => {
        const mealData = this.foodLogs[meal] || [];

        const totalCals = Math.round(
          mealData.reduce((sum, food) => sum + (food.nutritions?.kcal || 0), 0)
        );

        const calcIntake = this.output[meal] || 0;

        return {
          meal,
          totalCals,
          calcIntake,
        };
      });
    },
  },
  methods: {
    fetchEntries() {
      fetch(`/api/getEntries/${this.selectedDate}`, { method: "GET" })
        .then((response) => response.json())
        .then((data) => {
          if (data.entry) {
            this.foodLogs = {
              breakfast: data.entry.breakfast || [],
              lunch: data.entry.lunch || [],
              dinner: data.entry.dinner || [],
              snack: data.entry.snack || []
            };
          } else {
            this.foodLogs = {
              breakfast: [],
              lunch: [],
              dinner: [],
              snack: []
            }
          }
        })
        .catch((error) => {
          console.error("Fehler beim Abrufen der Daten:", error);
        });
    }
  },
  mounted() {
    this.fetchEntries();
  },
  watch: {
  selectedDate() {
    this.fetchEntries();
  }
}
};
</script>
