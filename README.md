# 🎬 Mood-Based Movie Recommendation System

A hybrid system that recommends movies based on the user's current mood, detected via facial expression analysis using MATLAB. The detected emotion is classified using an SVM (Support Vector Machine) model and sent to a Python Flask backend, which suggests movies mapped to that mood.

---

## 📌 Features

- ✅ Real-time facial expression detection using webcam
- ✅ Emotion classification using SVM in MATLAB
- ✅ Cross-platform communication between MATLAB and Flask (via HTTP or file system)
- ✅ Mood-to-genre mapping for personalized movie recommendations
- ✅ Flask-based REST API for backend logic and frontend display

---

## 🔧 Technologies Used

| Layer         | Technology         |
|---------------|--------------------|
| Emotion Detection | MATLAB (Image Processing Toolbox, SVM Classifier) |
| Backend API   | Python Flask       |
| Movie Dataset | CSV / SQLite / TMDB API (optional) |
| Communication | HTTP Requests / File-based Integration |
| Frontend      | HTML, CSS (optional Flask template) |

---

## 📁 Project Structure

```plaintext
Mood-Based-Movie-Recommendation-System/
│
├── matlab/
│   ├── emotion_detection.m           # Captures and classifies facial expressions
│   ├── svm_model.mat                 # Pre-trained SVM model
│   └── send_to_flask.m               # Sends detected mood to Flask backend
│
├── flask_app/
│   ├── app.py                        # Flask server
│   ├── mood_genre_map.py            # Mood to genre mapping
│   ├── movies.csv                   # Sample movie dataset
│   ├── templates/
│   │   └── index.html                # Optional frontend
│   └── static/                      # Optional styling/assets
│
├── README.md
└── requirements.txt                 # Python dependencies
