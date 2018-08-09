from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import random
import string
from uuid import uuid4

# Create your views here.
matching_queue = []

def index(request):
  if len(matching_queue) == 0:
    room_name = str(uuid4())
    matching_queue.append(room_name)
  else:
    room_name = matching_queue.pop()
  # room_name_dict = {'room_name': room_name}
  return render(request, 'chat/index.html', {'room_name': mark_safe(room_name)})

def room(request, room_name, turn):
  print(request.POST)
  context = {'room_name': mark_safe(room_name), 'turn': turn}
  print(context)
  return render(request, 'chat/room.html', context)