import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

from chats.models import Chat
from rooms.models import Member


class ChatConsumer(AsyncWebsocketConsumer):
    @sync_to_async
    def get_room(self):
        return Member.objects.get(member=self.user).room

    @sync_to_async
    def create_message(self, message):
        Chat.objects.create(writer=self.user, message=message, room_id=self.room)

    async def connect(self):

        # 유저를 찾고, 유저가 들어가있는 방을 찾아야 함
        self.user = self.scope['user']
        self.room = await self.get_room()
        self.room_name = self.room.id
        self.room_group_name = 'chat_%s' % self.room_name
        print(self.room_name)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # DB에 추가 / 유저가 누군지 / 유저가 속해있는 방이 어딘지만 알면 됨
        await self.create_message(message=message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))