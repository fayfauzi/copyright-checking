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
