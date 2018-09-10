from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
  url(r'^ws/matching/(?P<user_id>[^/]+)/$', consumers.AsyncMatchingConsumer),
  url(r'^ws/chat/(?P<room_name>[^/]+)/(?P<turn>[FS])/$', consumers.AsyncChatConsumer),
]