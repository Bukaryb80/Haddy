from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Basic knowledge base
knowledge_base = {
    "pillcam": "PillCam Genius is a capsule endoscopy system used for gastrointestinal diagnostics.",
    "cloud reader": "PillCam Cloud Reader allows remote access to capsule endoscopy data.",
    "rtv": "RTV is a real-time viewer for endoscopy procedures.",
    "account setup": "To set up a service user account, go to the admin portal and assign permissions.",
    "technical requirements": "Minimum requirements include Windows 10, 8GB RAM, and Chrome browser."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = "I'm sorry, I don't have an answer for that yet."

    for key in knowledge_base:
        if key in user_input:
            response = knowledge_base[key]
            break

    return jsonify({"response": response})

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    text = data.get("text", "")
    target_lang = data.get("target", "en")
    translated = translator.translate(text, dest=target_lang)
    return jsonify({"translated_text": translated.text})

if __name__ == "__main__":
    app.run(debug=True)
