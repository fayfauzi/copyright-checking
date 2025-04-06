# 📸 Copyright Image Checker

A web application that allows users to upload images and checks for copyright infringement using a mock AI backend. This application helps users understand whether an image is potentially copyrighted or not by simulating AI detection based on the filename.

## Features

- **Image Upload**: 
  - Users can upload an image via the browser, and it will be sent to the backend for processing.

- **Copyright Check**: 
  - The application sends the uploaded image to the backend, which performs a mock AI check for copyright infringement.

- **Result Display**: 
  - After the backend processes the image, the result is displayed to the user, including:
    - **file_id**: Unique identifier for the uploaded file.
    - **verdict**: "Copyright Infringed" or "No Issue".
    - **confidence**: Percentage of confidence in the result (mocked for demo purposes).

- **Material Design UI**: 
  - The frontend uses Vue.js and basic CSS for a clean, user-friendly design. The interface is responsive and easy to use.

## Technologies Used

- **Vue.js**: Front-end framework used to build the app.
- **Flask**: Python backend framework to handle API requests.
- **CORS**: Enabled on the backend to allow frontend-backend communication during development.
- **Random AI Simulation**: Mock AI logic to simulate copyright detection based on the filename.
- **CSS**: For styling the application.

## File Structure

```plaintext
copyright-checker/
├── BE/
│   ├── app.py
├── FE/
│   ├── src/
│   │   └── components/
│   │       └── ImageUpload.vue
│   ├── public/
│   │   └── index.html
│   ├── main.js
└── README.md
```

## Setup Instruction

## 🔧 Backend (Flask)
1. Go to the BE/ folder:

cd backend

2. Create and activate a virtual environment (optional but recommended):
python -m venv venv
venv\Scripts\activate   # On Windows

3. Install dependencies:

pip install -r requirements.txt

4. Start the Flask API:
   
python app.py


By default, the backend will run at:
http://localhost:5000

## 💻 Frontend (Vue.js)
1. Go to the FE/ folder:
   
cd frontend

2.Install dependencies:

npm install

3.Run the development server:

npm run dev

By default, the frontend will run at:
http://localhost:5173

## API Integration notes 
- Endpoint: POST /api/check-copyright

- Content-Type: multipart/form-data

- Form Field: image (file)

✅ Sample Response:

{
  "file_id": "abc123",
  "verdict": "Copyright Infringed",
  "confidence": 87.5
}


## Assumptions & Design Choices

- No actual AI model is used — this is mock logic using filename-based detection.

- Confidence is simulated using random.uniform() for demonstration purposes.

- File ID is a short UUID used to uniquely identify uploads.

- All files are processed in-memory; no saving or database integration is implemented.

- CORS is enabled to allow frontend-backend communication during development.

- Simplicity and readability were prioritized for clarity.

