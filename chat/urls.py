from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?P<room_name>[^/]+)/(?P<turn>[FS])/$', views.room, name='room'),
  url(r'^after_chat/$', views.after_chat, name='after_chat'),
  url(r'^end_of_session/$', views.end_of_session, name='end_of_session'),
  url(r'^thanks/$', views.thanks, name='thanks'),
]