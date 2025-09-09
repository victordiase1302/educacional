import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.template.loader import get_template


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.GROUP_NAME = 'user-notifications'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )

    def user_mensage(self, event):
        html = get_template('development/components/notification.html').render(
            context={
                'message': event['text'], 
                'color': event['color'],
                'emoji': event['emoji'],
                'link': event['link'],
                'id_notification': event['id_notification'],
                'site_active': event['site_active'],
            }
        )
        self.send(text_data=html)

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json["message"]

    #     self.send(text_data=json.dumps({"message": message}))