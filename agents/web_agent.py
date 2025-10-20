#!/usr/bin/env python3
from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)
OLLAMA_API_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"
history = []

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Agent IA Local</title>
    <style>
        body { font-family: sans-serif; margin: 2em; }
        .user { color: blue; }
        .assistant { color: green; margin-bottom: 1em; }
        textarea { width: 100%; height: 100px; }
        input[type=submit] { margin-top: 10px; }
    </style>
</head>
<body>
    <h1>💬 Agent IA Local ({{ model }})</h1>
    {% for m in messages %}
        <div class="{{ m.role }}">
            <strong>{{ m.role.capitalize() }} :</strong> {{ m.content }}
        </div>
    {% endfor %}
    <form method="POST">
        <textarea name="prompt" placeholder="Posez une question..." required></textarea><br>
        <input type="submit" value="Envoyer">
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def chat():
    global history

    if request.method == "POST":
        user_input = request.form["prompt"]
        history.append({"role": "user", "content": user_input})

        payload = {
            "model": MODEL,
            "messages": history,
            "stream": False
        }

        response = requests.post(OLLAMA_API_URL, json=payload)
        if response.status_code == 200:
            reply = response.json()["message"]["content"]
            history.append({"role": "assistant", "content": reply})
        else:
            history.append({"role": "assistant", "content": "⚠️ Erreur lors de la requête à Ollama."})

    return render_template_string(HTML_TEMPLATE, messages=history, model=MODEL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)