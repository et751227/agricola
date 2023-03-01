#載入LineBot所需要的模組
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from .scraper import YahooStock

import os

line_bot_api = LineBotApi(os.getenv("LINE_CHANNEL_ACCESS_TOKEN"))
line_handler = WebhookHandler(os.getenv("LINE_CHANNEL_SECRET"))

app = Flask(__name__)

#首頁測試
@app.route('/')
def home():
    return 'Hello, World!'
    
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
 
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
 
    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####

@line_handler.add(MessageEvent, message=TextMessage)

def handle_message(event):

    message = event.message.text
    
    if "股利 " in message:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
    else:
        stock = YahooStock(message)    
        reply_message = TextSendMessage(text=stock.scrape())
    
        line_bot_api.reply_message(event.reply_token,reply_message)
    
if __name__ == "__main__":
    app.run()