<template>
    <footer class="footer">
      <div class="grid-container">
        <RouterLink class="grid-item diary" to="/">
            <font-awesome-icon  icon="book"/>
            <span>diary</span>
        </RouterLink>
        <div class="grid-item add-meal">
            <ImageUpload class="add-btn"/>
        </div>
        <RouterLink class="grid-item profile" to="/profile">
            <font-awesome-icon icon="user"/>
            <span>profile</span>
        </RouterLink>
      </div>
    </footer>
</template>

<script>
import ImageUpload from './ImageUpload.vue';

    export default {
        name: "FooterBar",
        components: {
            ImageUpload
        }
    };
</script>

<style scoped>
.footer {
    background-color: #F7F7F7;
    position: fixed; /* Optional: Macht den Footer immer sichtbar */
    bottom: 0;
    left: 0;
    width: 100%;
    height: 82px;
}
.grid-container{
    display: inline-grid;
    grid-auto-flow: column;
    gap: 10px;
    height: 35px;
    width: 100%;
    padding: 1.2rem 2rem;
}
.grid-item{
    align-items: center;
    display: flex;
    flex-direction:column;
    justify-content: center;
    text-align: center;
}
.diary, .profile{
    color: #888888;
}
.add-meal{
    position: relative;
}
.add-btn{
    position: absolute;
    top:-50px;
    width: 75px;
    height: 75px;
}
</style>
