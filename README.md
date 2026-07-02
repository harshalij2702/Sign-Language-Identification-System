# Sign Language Identification System

## Description
The Sign Language Identification System is a web-based application developed to recognize sign language alphabet gestures from uploaded images using a Convolutional Neural Network (CNN). The system processes the input image, predicts the corresponding sign language letter, and displays the result through a user-friendly web interface. The project combines machine learning with full-stack web development to provide an interactive and efficient sign language recognition solution.

---

## Technologies Used

### Frontend
- React.js
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask
- REST API

### Machine Learning
- TensorFlow
- Keras
- Convolutional Neural Network (CNN)
- OpenCV
- NumPy
- Pillow

### Database
- PostgreSQL

---

## Features

- Upload sign language images for prediction
- Recognize alphabet gestures using a trained CNN model
- Fast and accurate prediction results
- Flask REST API for backend processing
- Responsive React.js user interface
- Easy-to-use web application

---

## Project Structure

```
Sign-Language-Identification-System/
│
├── backend/
│   ├── app.py
│   ├── sign_language_model.pkl
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
```

---

## Installation

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## How It Works

1. Upload a sign language image.
2. The Flask backend receives the image.
3. The trained CNN model processes the image.
4. The predicted alphabet is generated.
5. The result is displayed in the React.js application.

---

## Future Enhancements

- Real-time sign language recognition using a webcam
- Word and sentence prediction
- Support for dynamic hand gestures
- Improve prediction accuracy with a larger dataset
- Deploy the application to the cloud

---

## Author

**Harshali Janjalkar**

Python Developer | React.js | Flask | PostgreSQL | Machine Learning
