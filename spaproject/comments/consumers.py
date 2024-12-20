from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'comments'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        
    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'new_comment',
                'message': data['message']
            }
        )

    async def new_comment(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'type': 'new_comment',
            'message': message
        }))

    async def update_likes(self, event):
        await self.send(text_data=json.dumps({
            "type": "update_likes",
            "id": event["message"]["id"],
            "likes": event["message"]["likes"],
            "dislikes": event["message"]["dislikes"]
        }))