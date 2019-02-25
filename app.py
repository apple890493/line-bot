#用python寫伺服器有兩種套件,flask(小規模).django(網頁) ;網站=伺服器
#web app 首要檔案都是app.py

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('nBIbNhJPIr1GDNOXtgC/ZBbLcxdIHcJR2DNuMl88G8HTw+TG0zRTBV7QfJBUkV22dgKog0HD9skdo67gr2O++FXIgP59F9Ivoa0Zas5jw7WAvTTjOruOraW+7AJGpxaEk2nnifGnCkMHjLAU5mKcWAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4bbd8fb2a969aa4eeb780312b2187bdc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run() 