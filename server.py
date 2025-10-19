"""
Web deployment server for the Emotion Detection application using Flask.
This application exposes two routes: one for the homepage and one for
processing text to detect emotions using the Watson NLP library.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
# Pylint requires the app object to be a global constant, hence the name
APP = Flask("Emotion Detector")

@APP.route("/")
def render_index_page():
    """Renders the main index.html page."""
    return render_template('index.html')

@APP.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Run the emotion detector function
    response = emotion_detector(text_to_analyze)

    # Check for invalid text or API failure (where dominant_emotion is None)
    if response is None or response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Extract results and the dominant emotion, providing defaults for safety
    anger = response.get('anger', 0.0)
    disgust = response.get('disgust', 0.0)
    fear = response.get('fear', 0.0)
    joy = response.get('joy', 0.0)
    sadness = response.get('sadness', 0.0)
    dominant_emotion = response['dominant_emotion']

    # Format the output string exactly as requested by the customer
    formatted_output = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return formatted_output

if __name__ == '__main__':
    """Main execution block: deploys the Flask application."""
    # Deploy the application on localhost:5000
    APP.run(host="0.0.0.0", port=5000)