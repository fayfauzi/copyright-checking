<script setup lang="ts">
import { ref } from 'vue'

const selectedFile = ref(null)
const result = ref(null)

function handleFileChange(event) {
  selectedFile.value = event.target.files[0]
  result.value = null
}

async function uploadFile() {
  if (!selectedFile.value) return

  const formData = new FormData()
  formData.append('image', selectedFile.value)

  try {
    const response = await fetch('http://localhost:5000/api/check-copyright', {
      method: 'POST',
      body: formData
    })

    const data = await response.json()
    result.value = data
  } catch (error) {
    console.error('Error uploading file:', error)
    result.value = { verdict: 'Error uploading file' }
  }
}
</script>

<template>
  <div class="upload-container">
    <h2>Upload Image</h2>
    <input type="file" @change="handleFileChange" accept="image/*" />
    <button @click="uploadFile" :disabled="!selectedFile">Upload</button>

    <div v-if="result" class="result">
      <p><strong>File ID:</strong> {{ result.file_id }}</p>
      <p><strong>Verdict:</strong> {{ result.verdict }}</p>
      <p><strong>Confidence:</strong> {{ result.confidence }}%</p>
    </div>
  </div>
</template>

<style scoped>
.upload-container {
  padding: 20px;
  border: 2px dashed #ccc;
  max-width: 400px;
  margin: auto;
  border-radius: 8px;
  text-align: center;
}

.result {
  margin-top: 20px;
  font-size: 1.1em;
  color: #333;
}
</style>
