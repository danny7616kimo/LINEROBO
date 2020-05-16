



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

line_bot_api = LineBotApi('W6iqKj5qVGYEC5an8hrgn5sGryTwIsEW9SRGPXrjWmSpZmHYd9CDbHc8ciBxh6XhtslIu/AP+pbiWf4eE1vU9mqiciAFV0Ro4HpzIUDCIYNh03lU0qdU7+sISikE7CtEMMr8V73BmeoutD5qN27PNQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e735cd54613be84958bbb5ce24da7f6b')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

    