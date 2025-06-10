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

```

## 🚀 **How It Works**

### 🎭 Face Detection and Emotion Classification (MATLAB):

- Captures image from webcam.
- Extracts facial features.
- Classifies emotion using a pre-trained SVM model.
- Sends the detected mood to the Flask server.

### 🎬 Mood Mapping and Movie Recommendation (Python Flask):

- Receives the mood.
- Matches mood to one or more movie genres.
- Selects movies from dataset or via API.
- Displays recommendations on a web interface or returns JSON.

---

## 💻 **Setup Instructions**

### ✅ Prerequisites

- MATLAB (with Image Processing & ML Toolboxes)
- Python 3.7+
- Flask
- scikit-learn, pandas, requests, etc.

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/ShashankBedre/Mood-Based-Movie-Recommendation-System.git
cd Mood-Based-Movie-Recommendation-System
```

## 🐍 2. Set Up Python Environment

cd flask_app
pip install -r requirements.txt
python app.py

## 📷 3. Run MATLAB Script

- Open emotion_detection.m in MATLAB.
- Make sure your webcam is connected.
- Run the script. It will:
  - Detect your facial expression.
  - Classify the emotion.
  - Send the result (e.g., "Happy") to the Flask server.
 
## 🧠 Mood-to-Genre Mapping (Example)

| Mood      | Genres              |
| --------- | ------------------- |
| Happy     | Comedy, Romance     |
| Sad       | Drama, Inspiration  |
| Angry     | Action, Thriller    |
| Surprised | Mystery, Adventure  |
| Neutral   | Sci-Fi, Documentary |

## 📷 Screenshots (Optional)

Screenshots of:
 - MATLAB emotion detection
 - Classified mood output
 - Flask interface with movie recommendations

## 📌 TODOs / Future Work
 - Enhance face detection using CNN or deep learning models
 - Use real-time video instead of static webcam capture
 - Add user login (OAuth) and profiles for personalized watchlists
 - Integrate The Movie Database (TMDB) API for real-time movie data

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

## 🤝 Acknowledgements
 - MATLAB Documentation

 - Flask Documentation
 
 - The Movie Database (TMDB) API
