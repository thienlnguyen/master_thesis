<template>
    <div>
        <span class="heading">profile</span>
        <div class="user-detail">
            <div class="grid-container">
                <div class="label">name:</div>
                <div class="value">{{ user.userInfo.name }}</div>

                <div class="label">age:</div>
                <div class="value">{{ user.userInfo.age }}</div>

                <div class="label">height:</div>
                <div class="value">{{ user.userInfo.height_in_cm }} cm</div>

                <div class="label">weight:</div>
                <div class="value">{{ user.userInfo.weight_in_kg }} kg</div>

                <div class="label">activity level:</div>
                <div class="value">{{ activityLevel.name }}</div>

                <div class="label">goal:</div>
                <div class="value">{{ goal.goal }}</div>
            </div>
        </div>

    </div>
</template>

<script>
    import data from "../../data/data.json";
export default{
    name: "ProfileInfo",
    data() {
        return {
            user: data.user,
            activityLevels: data.activityLevels,
            goals: data.goals
        };
    },
    computed: {
        activityLevel(){
            return this.activityLevels.find (
                (level) => level.id === this.user.goals.activityLevel
            );
        },
        goal(){
            return this.goals.find(
                (goal) => goal.id === this.user.goals.goal
            )
        }
    }
}
</script>

<style scoped>
.heading{
    font-size: 12px;
    color: #888888;
    font-weight: bold;
}
.grid-container {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 5px 16px;
}

.label {
    font-weight: bold;
    text-align: left;
    color: #888888;
    font-size: 12px
}
.user-detail{
    border: 1px solid #CECECE;
    border-radius: 10px;
    padding: 1rem;
    margin-bottom: 1rem;
}
.value{
    color: #888888;
    font-size: 12px;
}
</style>
