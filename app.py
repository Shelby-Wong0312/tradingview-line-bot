from flask import Flask, request
from line import send_line_message
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "⚠️ TradingView 警報觸發！")
    send_line_message(message)
    return 'OK'

@app.route('/')
def home():
    return 'Webhook is running.'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

