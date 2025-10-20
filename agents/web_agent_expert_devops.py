from flask import Flask, request, render_template_string
import requests
# import os

app = Flask(__name__)

MODEL = "llama3"
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# Lire le prompt système depuis le fichier texte
PROMPT_PATH = "./prompts/devops.txt"
with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    system_prompt = f.read()

# Initialisation de l'historique avec le prompt système
history = [{"role": "system", "content": system_prompt}]

# Interface HTML minimaliste
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Agent DevOps</title>
</head>
<body>
    <h2>💬 Agent IA DevOps</h2>
    <form method="post">
        <label>Vous :</label><br>
        <textarea name="user_input" rows="4" cols="80" autofocus></textarea><br><br>
        <input type="submit" value="Envoyer">
    </form>
    {% if response %}
        <h3>🧠 Réponse de l'agent :</h3>
        <div style="white-space: pre-wrap;">{{ response }}</div>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        history.append({"role": "user", "content": user_input})

        payload = {
            "model": MODEL,
            "messages": history
        }

        r = requests.post(OLLAMA_API_URL, json=payload)
        r.raise_for_status()
        result = r.json()

        reply = result["message"]["content"]
        history.append({"role": "assistant", "content": reply})
        response = reply

    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    print("✅ Serveur Flask en cours de démarrage...")
    app.run(host="0.0.0.0", debug=True, port=5001)
