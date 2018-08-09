from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json, random

from asgiref.sync import async_to_sync

# class ChatConsumer(WebsocketConsumer):
#   def connect(self):
#     self.room_name = self.scope['url_route']['kwargs']['room_name']
#     self.room_group_name = 'chat_{}'.format(self.room_name)

#     async_to_sync(self.channel_layer.group_add)(
#       self.room_group_name, self.channel_name)

#     self.accept()

#   def disconnect(self, close_code):
#     async_to_sync(self.channel_layer.group_discard)(
#       self.room_group_name, self.channel_name)

#   def receive(self, text_data):
#     text_data_json = json.loads(text_data)
#     message = text_data_json['message']

#     async_to_sync(self.channel_layer.group_send)(
#       self.room_group_name,
#       {
#         'type': 'chat_message',
#         'message': message
#       }
#     )

#   def chat_message(self, event):
#     message = event['message']
#     username = event['username']

#     self.send(text_data=json.dumps({'message': message, 'username':username}))

class AsyncChatConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    # self.user_name = self.channel_name
    self.room_group_name = 'chat_{}'.format(self.room_name)

    await self.channel_layer.group_add(
      self.room_group_name, self.channel_name)

    await self.accept()

  async def disconnect(self, close_code):
    await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

  async def receive(self, text_data):
    text_data_json = json.loads(text_data)
    message = text_data_json['message']
    sender_id = self.channel_name

    await self.channel_layer.group_send(
      self.room_group_name,
      {
        'type': 'chat_message',
        'message': message,
        'sender_id': sender_id,
      }
    )

  async def chat_message(self, event):
    message = event['message']
    if event['sender_id'] == self.channel_name:
      sender_name = 'あなた'
    else:
      sender_name = 'あいて'

    await self.send(text_data=json.dumps({'message':message, 'sender_name':sender_name}))


from collections import defaultdict
num_room_members = defaultdict(lambda:0)
class AsyncMatchingConsumer(AsyncWebsocketConsumer):
  async def connect(self):
    self.room_name = self.scope['url_route']['kwargs']['room_name']
    self.matching_group_name = 'matching_{}'.format(self.room_name)
    self.is_first = False

    await self.channel_layer.group_add(
      self.matching_group_name, self.channel_name)

    await self.accept()

  async def disconnect(self, close_code):
    await self.channel_layer.group_discard(self.matching_group_name, self.channel_name)
    num_room_members[self.matching_group_name] -= 1

  async def receive(self, text_data):
    data_json = json.loads(text_data)
    room_name = data_json['room_name']
    if num_room_members[self.matching_group_name] > 0:
      del num_room_members[self.matching_group_name]
      self.is_first = True
      await self.channel_layer.group_send(
        self.matching_group_name,
        {
          'type': 'matched',
          'room_name': self.room_name,
        }
      )
    else:
      num_room_members[self.matching_group_name] += 1

  async def matched(self, data):
    room_name = data['room_name']
    await self.send(text_data=json.dumps({'room_name': room_name, 'is_first': self.is_first}))