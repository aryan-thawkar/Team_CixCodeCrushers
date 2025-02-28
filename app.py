from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # This serves the HTML file

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # System message to enforce structured responses
    system_message = {
        "role": "system",
        "content": "Respond in a well-formatted manner using bold text, indentation, and line breaks where necessary. Format responses in HTML where applicable. act as a chatbot to conduct mock technical interviews with real-time feedback."
    }

    response = ollama.chat(model="llama3.2", messages=[system_message, {"role": "user", "content": user_input}])

    formatted_response = response["message"]["content"]

    return jsonify({"response": formatted_response})

if __name__ == "__main__":
    app.run(debug=True)
