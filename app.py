#載入LineBot所需要的模組
from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
 
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('mfhl7PgbcNUgrQtrOYY41eM4QFItaevgruxSqBysuQQnd/dNC5+PLcGbOQWpJDukJiNjo3E1ajdS6ZHG4TmIGeD4KcInWRyqcpEjDSlEOzvsjPBZxHGGSr2ck/ULU5ktwwXb9r6r6AU5GHvoHuFmMgdB04t89/1O/w1cDnyilFU=')
 
# 必須放上自己的Channel Secret
handler = WebhookHandler('64cd78a666a16bef0e5cf97957ef1e18')

line_bot_api.push_message('Ubc9d9f76cfd0b91f30d4fff7839ed4b0', TextSendMessage(text='農家樂機器人建置中'))

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)
    
    #主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)