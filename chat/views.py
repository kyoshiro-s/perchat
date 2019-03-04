from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json
import random
import string
from .persona import generate_random, get_attr_list
from .models import Worker, ChatRoom
from uuid import uuid4

# Create your views here.

def top(request):
  return render(request, 'chat/top.html')

def anteroom(request):
  persona = generate_random()
  return render(request, 'chat/anteroom.html', {'persona': persona})

def chatroom(request, room_name, turn):
  p_list = request.POST.getlist('persona')
  persona = [(k,v) for k,v in [p.split('=') for p in p_list]]

  context = {
    'room_name': mark_safe(room_name),
    'turn': turn,
    'persona': persona,
  }
  # print(context)
  persona_text = '&'.join(p_list)
  tmp_id = uuid4()
  Worker.objects.create(
    worker_id=tmp_id,
    seed_persona=persona_text,
    turn=turn,
    room=ChatRoom.objects.get(room_name=room_name),
    mail=request.POST.get('mail'),
  )
  return render(request, 'chat/chatroom.html', context)

def after_chat(request):
  room_name = request.POST['room_name']
  turn = request.POST['turn']
  worker = Worker.objects.get(
      room=ChatRoom.objects.get(room_name=room_name),
      turn=turn,
  )
  persona_list = [(k,v) for k,v in [p.split('=') for p in worker.seed_persona.split('&')]]
  context = {
    'room_name': room_name,
    'turn': turn,
    'worker': worker,
    'seed_persona': persona_list,
    'attributes': get_attr_list(),
  }
  return render(request, 'chat/after_chat.html', context)


def end_of_session(request):
  est_persona = zip(
    request.POST.getlist('estimated-attr-input'),
    request.POST.getlist('estimated-val-input')
  )
  sup_persona = zip(
    request.POST.getlist('sup-attr-input'),
    request.POST.getlist('sup-val-input')
  )
  worker_id = request.POST['worker_id']
  est_persona_text = '&'.join(['='.join(p) for p in [_ for _ in est_persona if _[0]!='' and _[1]!='']])
  sup_persona_text = '&'.join(['='.join(p) for p in [_ for _ in sup_persona if _[0]!='' and _[1]!='']])
  # print('est:', est_persona_text)
  # print('sup:', sup_persona_text)
  w = Worker.objects.get(worker_id=worker_id)
  w.sup_persona = sup_persona_text
  w.estimated_partner_persona = est_persona_text
  # print(w.sup_persona, w.estimated_partner_persona)
  w.save()
  return redirect('thanks', verifycode=worker_id)

def thanks(request, verifycode):
  return render(request, 'chat/thanks.html', {'verifycode': verifycode})