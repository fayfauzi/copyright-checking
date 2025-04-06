<script setup lang="ts">
import { ref } from 'vue'

const file = ref(null)   // Holds the selected file
const status = ref('')   // Holds the upload status message

// Handle file change
const handleFileChange = (event) => {
  const selectedFile = event.target.files[0]
  if (selectedFile) {
    file.value = selectedFile
  }
}

// Handle file upload
const uploadFile = async () => {
  if (!file.value) return
  
  const formData = new FormData()
  formData.append('image', file.value)

  try {
    // Send the file to the backend (Replace with your actual backend URL)
    const response = await fetch('http://localhost:5000/api/check-copyright', {
      method: 'POST',
      body: formData
    })
    
    const result = await response.json()
    
    if (response.ok) {
      status.value = `Upload successful: ${result.result}`
    } else {
      status.value = `Error: ${result.result}`
    }
  } catch (error) {
    status.value = `Upload failed: ${error.message}`
  }
}
</script>

<template>
  <div id="app">
    <h1>Copyright Checker</h1>
    
    <!-- File Upload Form -->
    <input type="file" @change="handleFileChange" />
    
    <!-- Display File Information -->
    <div v-if="file">
      <p><strong>Selected File:</strong> {{ file.name }}</p>
      <p><strong>Size:</strong> {{ file.size }} bytes</p>
    </div>

    <!-- Upload Button -->
    <button @click="uploadFile" :disabled="!file">Upload</button>
    
    <!-- Display Upload Status -->
    <div v-if="status">{{ status }}</div>
  </div>
</template>

<style scoped>

</style>
