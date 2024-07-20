from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/', methods=['GET'])
def get_student_number():
    student_number = "12345678"  # Replace with your actual student number
    return jsonify({"student_number": student_number})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    intent = req.get('queryResult').get('intent').get('displayName')

    # Example of handling different intents
    if intent == 'AnimeStudioDetails':
        response_text = "This is the response for AnimeStudioDetails intent."
    elif intent == 'AnimeRecommendation':
        response_text = "This is the response for AnimeRecommendation intent."
    else:
        response_text = "I'm not sure how to respond to that."

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
