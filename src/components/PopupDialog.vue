
<template>
  <div v-if="isVisible" class="overlay" @click.self="cancel">
    <div class="popup">
      <h2 class="popup-title">{{ title }}</h2>
      <p class="popup-message">{{ message }}</p>
      <div class="popup-buttons">
        <button @click="cancel" class="popup-btn cancel-btn">Abbrechen</button>
        <button @click="confirm" class="popup-btn submit-btn">{{ submitLabel }}</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    message: String,
    submitLabel: {
      type: String,
      default: "OK",
    },
    isVisible: Boolean,
    itemId: Number,
  },
  emits: ["confirm", "cancel"],
  methods: {
    confirm() {
      this.$emit("confirm", this.itemId);
    },
    cancel() {
      this.$emit("cancel");
    },
  },
};
</script>


<style scoped>
/* Hintergrund für das Popup */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

/* Popup-Styling */
.popup {
  background: #fff;
  width: 300px;
  padding: 20px;
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
  text-align: center;
  font-family: "SF Pro Display", sans-serif;
}

.popup-title {
  font-size: 18px;
  font-weight: 600;
  color: #888888;
}

.popup-message {
  font-size: 14px;
  color: #888888;
  margin-top: 10px;
}

.popup-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 15px;
}

.popup-btn {
  flex: 1;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  font-weight: 500;
}

.cancel-btn {
  background: #f1f1f1;
  color: #333;
  border-radius: 10px;
  margin-right: 10px;
}

.submit-btn {
  background: #6D91CD;
  color: #fff;
  border-radius: 10px;
}
</style>
