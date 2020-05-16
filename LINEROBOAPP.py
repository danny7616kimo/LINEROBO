



from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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
	msg = event.message.text
	r = '請你再說一次'

	if '貼圖' in msg:
		sticker_message = StickerSendMessage(
	    package_id='1',
	    sticker_id='1'
	)
	line_bot_api.reply_message(
	event.reply_token,
	sticker_message)	
	return


	if msg in ['strong', '壯']:
		r = 'go get it'
	elif ['預算' or '錢' or '價'] in msg:
		r = '衝阿 專心工作'
	elif ['預約' or '晚上' or '空位'] in msg:
		r = '請問是要定位嗎? 幾個人?'

	line_bot_api.reply_message(
		event.reply_token,
		TextMessage(text=r))


if __name__ == "__main__":
	app.run()

	