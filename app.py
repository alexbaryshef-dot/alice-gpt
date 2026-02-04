from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

OPENAI_API_KEY = "ТУТ_ТВОЙ_КЛЮЧ"

@app.route('/', methods=['POST'])
def alice():
    data = request.json
    user_text = data['request']['original_utterance']

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": user_text}]
    }

    r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    answer = r.json()['choices'][0]['message']['content']

    return jsonify({
        "response": {"text": answer, "end_session": False},
        "version": "1.0"
    })

if __name__ == '__main__':
    app.run()
