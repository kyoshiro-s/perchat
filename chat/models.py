from django.db import models
from uuid import uuid4

class Worker(models.Model):
  worker_id = models.CharField(max_length=30, unique=True)
  persona = models.CharField(max_length=50)
  room = models.ForeignKey('ChatRoom', to_field='room_name', on_delete=models.CASCADE)
  turn = models.CharField(max_length=1)

  def __str__(self):
    return '<{}>'.format(self.worker_id)



class ChatRoom(models.Model):
  room_name = models.CharField(max_length=30, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '<{}>'.format(self.room_name)



class ChatMessage(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  room = models.ForeignKey('ChatRoom', to_field='room_name', on_delete=models.CASCADE)
  sender = models.ForeignKey('Worker', to_field='worker_id', on_delete=models.CASCADE)
  text = models.CharField(max_length=200)

  def __str__(self):
    return '<{}: {}>'.format(self.sender, self.text)