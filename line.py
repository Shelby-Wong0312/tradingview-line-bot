import requests
import os

def send_line_message(msg):
    token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
    user_id = os.getenv("LINE_TO_ID")
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": user_id,
        "messages": [{"type": "text", "text": msg}]
    }
    r = requests.post(url, headers=headers, json=payload)
    print(r.status_code, r.text)
