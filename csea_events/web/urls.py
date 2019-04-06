from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gettoken/$', views.gettoken, name='gettoken'),
    url(r'^web/$', views.index, name='index')
]
