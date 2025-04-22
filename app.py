from flask import Flask, request
from line import send_line_message
import os
import sys

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
@app.route('/debug', methods=['POST'])
def debug():
    print("🟢 DEBUG START")
    sys.stdout.flush()
    print("Raw headers:", dict(request.headers))
    sys.stdout.flush()
    print("Raw body:", request.data.decode('utf-8'))
    sys.stdout.flush()
    print("🟢 DEBUG END")
    sys.stdout.flush()
    return 'OK'

@app.route('/test')
def test_message():
    send_line_message("✅ 測試成功，這是從 Render 發出的 LINE 訊息！")
    return "測試訊息已發送"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("🟡 WEBHOOK START")
    print("Raw JSON:", data)
    sys.stdout.flush()

    message = data.get("message", "⚠️ TradingView 警報觸發！")
    print("Extracted message:", message)
    sys.stdout.flush()

    send_line_message(message)
    return 'OK'
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

