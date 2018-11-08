from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.top, name='top'),
  url(r'^anteroom/$', views.anteroom, name='anteroom'),
  url(r'^(?P<room_name>[^/]+)/(?P<turn>[FS])/$', views.chatroom, name='chatroom'),
  url(r'^after_chat/$', views.after_chat, name='after_chat'),
  url(r'^end_of_session/$', views.end_of_session, name='end_of_session'),
  url(r'^thanks/(?P<verifycode>[^/]+)/$', views.thanks, name='thanks'),
]