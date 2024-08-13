from django.shortcuts import render
from django.views.generic import TemplateView

from src.apps.whisper.main import NotificationService


# Create your views here.
class HomeView(TemplateView):
  #  email = NotificationService('asd', 'asd', 'asd', )
  #  email.send_email_notification_smtp('whisper/emailnotification_list.html','saqiba@gmail.com')
    template_name = 'website/index.html'
