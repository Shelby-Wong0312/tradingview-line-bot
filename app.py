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
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

