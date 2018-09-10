from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
import random
import string
from .persona import generate_random
from .models import Worker, ChatRoom
from uuid import uuid4

# Create your views here.

def index(request):
  persona = generate_random()
  return render(request, 'chat/index.html', {'persona': persona})

def room(request, room_name, turn):
  p_list = request.POST.getlist('persona')

  persona = {k:v for k,v in [p.split('=') for p in p_list]}
  # ↑は↓と同義
  # persona = dict()
  # for p in p_list:
  #   k, v = p.split(':')
  #   persona[k] = v

  context = {
    'room_name': mark_safe(room_name),
    'turn': turn,
    'persona': persona,
  }
  print(context)

  persona_text = '&'.join(p_list)
  tmp_id = uuid4()

  Worker.objects.create(
    worker_id=tmp_id,
    persona=persona_text,
    turn=turn,
    room=ChatRoom.objects.get(room_name=room_name)
  )

  return render(request, 'chat/room.html', context)