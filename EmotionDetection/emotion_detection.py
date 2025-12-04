import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    return_dict = {}
    if response.status_code == 200:
        emotion_dict = formatted_response["emotionPredictions"][0]["emotion"]
        anger_score = emotion_dict["anger"]
        disgust_score = emotion_dict["disgust"]
        fear_score = emotion_dict["fear"]
        joy_score = emotion_dict["joy"]
        sadness_score = emotion_dict["sadness"]

        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        
        return_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }
    elif response.status_code == 400:
        return_dict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }

    return return_dict