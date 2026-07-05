from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message.strip():
        return jsonify({"response": "Say something! Don't be shy! 💜", "exit": False})

    result = get_response(user_message)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)