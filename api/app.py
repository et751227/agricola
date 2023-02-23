#載入LineBot所需要的模組
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import os
line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_bot_api_text = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
handler_text = os.getenv("LINE_CHANNEL_SECRET")

app = Flask(__name__)

#首頁測試
@app.route('/')
def home():
    return 'Hello, World!'
    return line_bot_api_text
    return handler_text

if __name__ == "__main__":
    app.run()