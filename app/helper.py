import requests
import json


def send_message(url: str, chat_id: int, text: str) -> None:
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    message = {
        "chat_id": chat_id,
        "text": text
    }
    payload = json.dumps(message)
    requests.get(url, data=payload, headers=headers)

