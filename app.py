from flask import Flask, render_template, request
from new_recommender_system import get_mood_based_recommendations  # Ensure this is your correct module

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Default emotion
    emotion = "neutral"

    try:
        # Adjust file path if needed, and ensure the file exists
        with open("C:\\xampp\\htdocs\\movie recommender\\detected_emotion.txt", 'r') as f:
            lines = f.readlines()

            # Check if there are any lines in the file
            if lines:
                last_line = lines[-1].strip()

                # Extract emotion from the line if it contains 'Detected Emotion:'
                if "Detected Emotion:" in last_line:
                    emotion = last_line.split(":")[-1].strip()
                else:
                    emotion = "neutral"  # If the line format is unexpected, default to 'neutral'
            else:
                emotion = "neutral"  # If file is empty, default to 'neutral'

    except FileNotFoundError:
        print("detected_emotion.txt not found. Defaulting to 'neutral'.")
        emotion = "neutral"
    except Exception as e:
        print(f"Error reading file: {e}")
        emotion = "neutral"

    # Get recommendations based on detected emotion
    recommendations, posters, links = get_mood_based_recommendations(emotion)

    # Render the recommendations page with the detected emotion
    return render_template('recommendations.html',
                           title=emotion,
                           emotion=emotion,
                           recommendations=zip(recommendations, posters, links))

if __name__ == '__main__':
    app.run(debug=True)
