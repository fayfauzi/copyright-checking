# 📸 Copyright Image Checker

A simple web app built with **Vue.js** (frontend) and **Flask** (backend API) that allows users to upload an image and checks for copyright infringement using mock AI logic.

---

## 🚀 Features

- Upload an image via the browser
- Sends image to backend Flask API
- Receives structured AI result:
  - `file_id`
  - `verdict` (e.g., "Copyright Infringed")
  - `confidence` (e.g., 87.5%)
- Displays result on screen

## 🛠 Setup Instructions

### 🔧 Backend (Flask)

1. Go to the `backend/` folder:
   ```bash
   cd backend
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Start the Flask API:

bash
Copy
Edit
python app.py
By default, it runs at:
http://localhost:5000

💻 Frontend (Vue.js)
Go to the frontend/ folder:

bash
Copy
Edit
cd frontend
Install dependencies:

bash
Copy
Edit
npm install
Run the development server:

bash
Copy
Edit
npm run dev
By default, it runs at:
http://localhost:5173

🔗 API Integration Notes
Endpoint: POST /api/check-copyright

Content-Type: multipart/form-data

Form Field: image (file)

✅ Sample Response:
json
Copy
Edit
{
  "file_id": "abc123",
  "verdict": "Copyright Infringed",
  "confidence": 87.5
}
🧠 Assumptions & Design Choices
No actual AI model is used — this is mock logic using filename-based detection.

Confidence is simulated using random.uniform() for demonstration purposes.

File ID is a short UUID used to uniquely identify uploads.

All files are processed in-memory; no saving or database integration.

CORS is enabled to allow frontend-backend communication during development.

Simplicity and readability were prioritized to make the code easy to follow.

📂 Project Structure
css
Copy
Edit
copyright-checker/
├── backend/
│   ├── app.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   └── components/
│   │       └── ImageUpload.vue
│   └── main.js
├── screenshots/
│   └── web-ui.png
└── README.md
📘 Tech Stack
Frontend: Vue 3 + Vite + JavaScript

Backend: Python + Flask

Styling: Basic CSS (no external UI libraries used)

API Format: JSON with structured fields (file_id, verdict, confidence)
