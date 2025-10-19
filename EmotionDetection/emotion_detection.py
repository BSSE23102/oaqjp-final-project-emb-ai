import requests
import json

import requests
import json

# ... (The rest of the function definition remains the same up to requests.post) ...

def emotion_detector(text_to_analyze):
    # API details
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { 
        "raw_document": { 
            "text": text_to_analyze 
        } 
    }
    
    # Send the POST request
    response = requests.post(url, json=input_json, headers=headers)
    
    # --- Start of New Error Handling Logic ---
    
    # Check for HTTP Status Code 400 (Bad Request - often due to blank text)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Check for other non-200 successful response status codes
    if response.status_code != 200:
        print(f"API Error - Status Code: {response.status_code}")
        return None 

    # --- End of New Error Handling Logic ---

    try:
        # ... (The rest of the JSON parsing logic remains the same) ...
        response_dict = json.loads(response.text)
        
        # The API returns a list of predictions in 'emotionPredictions'.
        emotion_scores = response_dict['emotionPredictions'][0]['emotion']
        
        # Now, transform this into a list of dictionaries for easier processing (like the old format)
        emotion_list = [
            {'emotion': name, 'score': score} 
            for name, score in emotion_scores.items()
        ]

    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing JSON response or missing key: {e}")
        print(f"Raw Response Text: {response.text}")
        return None
    
    # ... (The rest of the dominant emotion calculation and return statement remains the same) ...
    formatted_output = {}
    dominant_emotion = {'emotion': '', 'score': -1}

    # ... (Logic to populate formatted_output) ...

    formatted_output['dominant_emotion'] = dominant_emotion['emotion']
    
    return formatted_output

# ✅ Test manually (optional)
if __name__ == '__main__':
    test_text = "I am so happy I am doing this."
    result = emotion_detector(test_text)
    print(f"Text: '{test_text}'")
    print("Formatted Output:")
    print(result)
