import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from decouple import config
from django.template.loader import get_template
from openai import OpenAI


class OpenaiConsumer(WebsocketConsumer):
    def connect(self):
        self.GROUP_NAME = 'chat-openai'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envie a mensagem para a API do chatbot e aguarde a resposta
        response_message = self.chat_bot_api(message)

        # Envie a mensagem de resposta de volta ao WebSocket
        self.send(text_data=json.dumps({
            'message': response_message
        }))

    def chat_bot_api(self, message):
        # Substitua 'YOUR_API_KEY' pela sua chave de API do GPT-3
        client = OpenAI(api_key=config("OPENAI"))
        chat_completion = client.completions.create(
            prompt=f'{message}\n\n###\n\n',
            model="davinci:ft-personal:fortune-beta-2023-11-22-02-08-07",
            stop="\n\n$$$",
            stream=True,
            temperature=0,
            max_tokens=150,
        )
        answer = ''
        for response in chat_completion:
            answer += response.choices[0].text
            # print(resposta_do_bot)
            # Se você só precisa da primeira parte da resposta
        return answer

