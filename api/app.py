#載入LineBot所需要的模組
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import os

app = Flask(__name__)

#首頁測試
@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()