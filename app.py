import os
from decouple import config
from flask import (
    Flask, request, abort
)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
app = Flask(__name__)
# get LINE_CHANNEL_ACCESS_TOKEN from your environment variable
line_bot_api = LineBotApi(
    config("2BTcvtsRseZiX1J4k9N/0uBtUz7qLiSM460SKqqaPHRjZOyT9LEN3voNP4HHSOgprrdcKnK4JlZLQ7LKefxojE5P0tKSXJhSr/yeRHrV6jzSj84DnKGGsH+eaAyD5tFPGlggxqMWUt54Pj2Ljh2vGgdB04t89/1O/w1cDnyilFU=",
           default=os.environ.get('2BTcvtsRseZiX1J4k9N/0uBtUz7qLiSM460SKqqaPHRjZOyT9LEN3voNP4HHSOgprrdcKnK4JlZLQ7LKefxojE5P0tKSXJhSr/yeRHrV6jzSj84DnKGGsH+eaAyD5tFPGlggxqMWUt54Pj2Ljh2vGgdB04t89/1O/w1cDnyilFU='))
)
# get LINE_CHANNEL_SECRET from your environment variable
handler = WebhookHandler(
    config("c43991598893172a39d5a6ef40a7c3a4",
           default=os.environ.get('c43991598893172a39d5a6ef40a7c3a4'))
)


@app.route("/callback", methods=['POST'])
def callback():
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
def handle_text_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)