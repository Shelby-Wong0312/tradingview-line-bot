from flask import Flask, request
from line import send_line_message
import os
import sys

app = Flask(__name__)

# 唯一的 webhook 處理器
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # 印出 raw payload 方便排查
    print("🟡 WEBHOOK START")
    sys.stdout.flush()

    data = request.get_json()
    print("Raw JSON:", data)
    sys.stdout.flush()

    # 取 message 欄位，沒值就走預設
    message = data.get("message", "⚠️ TradingView 警報觸發！")
    print("Extracted message:", message)
    sys.stdout.flush()

    send_line_message(message)

    print("🟡 WEBHOOK END")
    sys.stdout.flush()
    return 'OK'

# 根目錄測試
@app.route('/')
def home():
    return 'Webhook is running.'

# /debug endpoint 保留原樣
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

# /test endpoint 保留原樣
@app.route('/test')
def test_message():
    send_line_message("✅ 測試成功，這是從 Render 發出的 LINE 訊息！")
    return "測試訊息已發送"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
