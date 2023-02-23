#載入LineBot所需要的模組
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

import os

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"

app = Flask(__name__)
 
#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####

@app.route('/')

def home():
    return 'Hello, World!'
    
@app.route("/webhook", methods=['POST'])

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)
    
if __name__ == "__main__":
    app.run()