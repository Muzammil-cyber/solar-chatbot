from flask import Flask, request, jsonify
from chatbot import get_answer
from utils import clean_input

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"response": "Please provide a message."}), 400

    response = get_answer(clean_input(user_message))
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
