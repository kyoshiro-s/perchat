from django.contrib import admin

from .models import ChatRoom, Worker, ChatMessage


class ChatMessageInline(admin.TabularInline):
  model = ChatMessage
  extra = 0

class WorkerInline(admin.TabularInline):
  model = Worker
  extra = 0

class ChatRoomAdmin(admin.ModelAdmin):
  list_display = ('room_name', 'created_at')
  fields = ['room_name']
  inlines = [WorkerInline, ChatMessageInline]

class WorkerAdmin(admin.ModelAdmin):
  fields = ['worker_id',
            'room',
            'seed_persona',
            'sup_persona',
            'estimated_partner_persona']
  inlines = [ChatMessageInline]

admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Worker, WorkerAdmin)