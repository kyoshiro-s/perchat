from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import random
import string
from .persona import generate_random

# Create your views here.

def index(request):
  persona = generate_random()
  return render(request, 'chat/index.html', {'persona': persona})

def room(request, room_name, turn):
  print(request.POST)
  context = {'room_name': mark_safe(room_name), 'turn': turn}
  print(context)
  return render(request, 'chat/room.html', context)