<template>
  <div>
    <button class="custom-file-btn" @click="triggerFileInput">
      <font-awesome-icon class="btn-plus" icon="plus" />
    </button>

    <input type="file" ref="fileInput" @change="onFileSelected"/>

    <div v-if="selectedImage" class="image-preview-container">

      <div class="grey-bar">
        <div class="btn-cancel" @click="cancelUpload">
          <font-awesome-icon class="btn-xmark" icon="xmark" />
        </div>
      </div>

      <div>
        <div class="image-preview" :class="{analyzing: analyzing}">
          <img :src="selectedImage" alt="Selected Image" />
        </div>
        <span  v-if="analyzing" class="analyzing-text">analyzing photo</span>
      </div>

      <div v-if="!analyzing" class="buttons-container">
        <button class="btn-item choose" @click="uploadImage">choose photo</button>
        <button class="btn-item retake" @click="resetSelection">retake</button>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      selectedFile: null,
      selectedImage: null,
      analyzing: false,
    };
  },
  props:{
    typeOfMeal: {
      type: String,
      require: true}
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click();
    },
    onFileSelected(event) {
      const file = event.target.files[0];
      if (file) {
        this.selectedFile = file;
        this.selectedImage = URL.createObjectURL(file);
      }
    },
    uploadImage() {
      const formData = new FormData();
      formData.append("image", this.selectedFile);

      fetch(`${import.meta.env.VITE_API_BASE_URL}/upload`, {
        method: "POST",
        body: formData,
      })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        this.cancelUpload();
        this.analyzing = true;
        this.navigateToAddMeal(data);
      })
      .catch((error) => {
        console.error("Error uploading image:", error);
      });
    },
    resetSelection() {
      this.cancelUpload();
      this.$refs.fileInput.click()
    },
    cancelUpload() {
      this.selectedFile = null;
      this.selectedImage = null;
      this.$refs.fileInput.value = null;
    },
    navigateToAddMeal(data) {
      this.$router.push({
        name: "addMeal",
        params: {
          typeOfMeal: encodeURIComponent(this.typeOfMeal),
          imageUrl: encodeURIComponent(data.filepath),
          id: encodeURIComponent(data.id)
        }
      });
    }
  },
};

</script>

<style scoped>
.custom-file-btn {
  border-radius: 50%;
  background-color: #6D91CD;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  width: inherit;
  height: inherit;
}
.btn-plus {
  color: white;
  height: 50%;
}
input[type="file"] {
  display: none;
}
.image-preview-container{
  position: absolute;
  left: 0;
  z-index: 10000;
  background-color: white;
  width: 100%;
  height: 100%;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px
}
.image-preview {
  max-height: 470px;
  overflow: hidden;
  border-radius: 15px;
  margin: 2rem;
}
.image-preview img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 15px;
  object-position: center;
}
.btn-item{
  width:270px;
  height: 40px;
  color: white;
  border-radius: 50px;
  border: none;
  margin: 0 auto 15px auto;
  align-items: center;
  display: flex;
  justify-content: center;
  font-weight: bold;
}
.btn-item.choose{
  background-color: #6D91CD;
}
.btn-item.retake{
  background-color: #AAC0E6;
}
.grey-bar{
  width: 100%;
  height: 40px;
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
.analyzing{
  opacity: 0.5;
}
</style>





