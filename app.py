from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Ensure the API key is set as an environment variable
api_key = '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'


# Initialize the OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    completion = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": user_message,
            },
        ],
    )
    response_message = completion.choices[0].message.content
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)
