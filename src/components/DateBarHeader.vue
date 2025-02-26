<template>
  <header class="header">
    <div class="grid-container">
      <div class="grid-item left">
        <font-awesome-icon class="chevron" icon="chevron-left" @click="changeDate(-1)" />
      </div>
      <div class="grid-item date">
        {{ selectedDate }}
      </div>
      <div class="grid-item right">
        <font-awesome-icon class="chevron" icon="chevron-right" @click="changeDate(1)" />
      </div>
    </div>
  </header>
</template>

<script>
export default {
  props: {
    selectedDate: String
  },
  methods: {
    changeDate(days) {
      this.$emit("update-date", days);
    }
  }
};
</script>

<style scoped>
.header {
  background-color: white;
  position: fixed;
  width: 100%;
  height: 35px;
  left: 0;
  padding: 0 2rem;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.1), inset 0 -1px 0 rgba(0, 0, 0, 0.05);
  z-index: 1000;
}
.grid-container {
  display: flex;
  gap: 10px;
  height: 40px;
  width: 100%;
}
.grid-item {
  width: 33.3%;
  display: flex;
  align-items: center;
}
.grid-item.left {
  justify-content: flex-start;
}
.grid-item.date {
  justify-content: center;
  font-weight: bold;
  color: #888888;
  font-size: 18px;
}
.grid-item.right {
  justify-content: flex-end;
}
.chevron {
  height: 24px;
  color: #888888;
  cursor: pointer;
}
</style>
