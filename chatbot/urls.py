from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('speech/', views.speech_page, name='speech_page'),
    path('send_message/', views.send_message, name='send_message'),
    path('transcribe/', views.transcribe, name='transcribe'),
]