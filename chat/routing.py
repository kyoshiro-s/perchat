from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
  url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.AsyncChatConsumer),
  url(r'^ws/matching/(?P<room_name>[^/]+)/$', consumers.AsyncMatchingConsumer),
]