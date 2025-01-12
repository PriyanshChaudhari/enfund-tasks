# v1
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from asgiref.sync import sync_to_async

# from chatapp.models import Room,Message,User

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_slug']
#         self.roomGroupName = 'chat_%s' % self.room_name
        
#         await self.channel_layer.group_add(
#             self.roomGroupName,
#             self.channel_name
#         )
#         await self.accept()
        
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.roomGroupName,
#             self.channel_name
#         )
        
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         username = text_data_json["username"]
#         room_name = text_data_json["room_name"]
        
#         await self.save_message(message, username, room_name)     

#         await self.channel_layer.group_send(
#             self.roomGroupName, {
#                 "type": "sendMessage",
#                 "message": message,
#                 "username": username,
#                 "room_name": room_name,
#             }
#         )
        
#     async def sendMessage(self, event):
#         message = event["message"]
#         username = event["username"]
#         await self.send(text_data=json.dumps({"message": message, "username": username}))
    
#     @sync_to_async
#     def save_message(self, message, username, room_name):
#         print(username,room_name,"----------------------")
#         user=User.objects.get(username=username)
#         room=Room.objects.get(name=room_name)
        
#         Message.objects.create(user=user,room=room,content=message)

# v2
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from chatapp.models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.other_user_id = self.scope['url_route']['kwargs']['user_id']
        self.room_group_name = f'chat_{self.scope["user"].id}_{self.other_user_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = self.scope['user']
        receiver = await sync_to_async(User.objects.get)(id=self.other_user_id)

        await self.save_message(sender, receiver, message)

        await self.channel_layer.send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender.username,
                'receiver': receiver
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))

    @sync_to_async
    def save_message(self, sender, receiver, message):
        Message.objects.create(sender=sender, receiver=receiver, content=message)
