from flask import Flask, request, abort

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)

from linebot.models import AudioSendMessage


app = Flask(__name__)

configuration = Configuration(access_token='6L3EoTaaYarq2BdiVT8hP/yT6BdytNaFbXGs1vXIpw0MjTglefQF0Yo7IEybTmuCuTQtrJDg5+HpeUQFe/hV7WVEdYUzUlX0AfpVXN5j1eRZsrgYzmpz9e2iAntsdu+7+xv2PPCstWgD55AmxqskBwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('72becbe4ce8f6e63f5d457ae60daa526')

    

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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        
        response = parrot(event)
        if "語音" in event.message.text:
            audio_message = AudioSendMessage(
            original_content_url='https://github.com/Carpheny/new_repo/blob/7803612721cdc8711b9a4bdb57dc96d4f736f2bd/dad.mp3',
            duration=6000
            )
            response="我送給你的話：\n"
            line_bot_api.push_message(event.reply_token, audio_message)
        else:
            response = "I'm your fucking Dad:"+event.message.text
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=response)]
            )
        )

if __name__ == "__main__":
    app.run()