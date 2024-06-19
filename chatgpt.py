import requests
import json
import config

def get_chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {config.OPENAI_SECRET_KEY}'
    }

    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': prompt}]
    }

    response = requests.post(config.OPENAI_CHAT_URL, headers=headers, data=json.dumps(data))
    response_data = response.json()

    if response.status_code == 200:
        return response_data['choices'][0]['message']['content']
    else:
        return f"Error: {response_data['error']['message']}"
