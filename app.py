from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "YOUR_STUDENT_NUMBER"})

# Route to handle Dialogflow webhook requests
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    
    # Extract intent name from the request
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Example of handling different intents and generating responses
    if intent == 'AnimeStudioDetails':
        response_text = "Here is the information about the anime studio."
    elif intent == 'AnimeRecommendation':
        response_text = "Here are some anime recommendations."
    elif intent == 'AnimeByCharacter':
        response_text = "You can find anime recommendations based on characters."
    elif intent == 'AnimeGenre':
        response_text = "Here are anime recommendations based on genres."
    else:
        response_text = "I'm not sure how to respond to that."

    # Return the response in the required format
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
