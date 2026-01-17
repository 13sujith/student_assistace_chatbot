from flask import Flask, request, jsonify, render_template
from chatbot import ask_question

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data["query"]
    answer = ask_question(query)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
