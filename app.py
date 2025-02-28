from flask import Flask, request, jsonify, render_template
import ollama
import pyttsx3
import threading

app = Flask(__name__)

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speech speed
engine.setProperty("volume", 1.0)  # Maximum volume

# Global mute variable
mute = False

def speak_text(text):
    """Speaks the text if mute is off."""
    global mute
    if not mute:
        engine.say(text)
        engine.runAndWait()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/code")
def code():
    return render_template("code.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")
@app.route("/vid")
def vid():
    return render_template("vid.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    system_message = {
        "role": "system",
        "content": "Respond in a well-formatted manner using bold text, indentation, and line breaks where necessary. Format responses in HTML where applicable. Act as a chatbot to conduct mock technical interviews with real-time feedback."
    }

    response = ollama.chat(model="llama3.2", messages=[system_message, {"role": "user", "content": user_input}])
    formatted_response = response["message"]["content"]

    # Speak response in a separate thread (if not muted)
    threading.Thread(target=speak_text, args=(formatted_response,), daemon=True).start()

    return jsonify({"response": formatted_response})

@app.route("/toggle_mute", methods=["POST"])
def toggle_mute():
    """Toggles mute on/off and sends updated state."""
    global mute
    mute = not mute  # Toggle mute
    return jsonify({"mute": mute})

@app.route("/get_mute_status", methods=["GET"])
def get_mute_status():
    """Returns the current mute state."""
    return jsonify({"mute": mute})

if __name__ == "__main__":  
    app.run(debug=True) 