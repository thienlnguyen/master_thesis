<template>
  <header class="header">
    <RouterLink class="btn-cancel" to="/">
      <font-awesome-icon class="btn-xmark" icon="xmark"/>
    </RouterLink>
  </header>
</template>

<script>
export default {
  name: "HeaderBar",
  data (){
      return {
          currentDate: new Date().toLocaleDateString("de-DE"),
      }
  },
  methods:{
    cancelUpload() {
      this.$router.push({
        name: "/",
      });
  },
}
}
</script>
<style scoped>
.header {
  position: fixed;
  left:0;
  padding:0 2rem;
  z-index: 1000;
  width: 100%;
  height: 45px;
  background-color: #F7F7F7F7;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  padding: 0 1rem;
}
.btn-xmark {
color: #888888;
height: 35px;
width: 35px
}
.btn-cancel {
height: 40px;
border: none;
align-items: center;
display: flex;
justify-content: end;
}
</style>
