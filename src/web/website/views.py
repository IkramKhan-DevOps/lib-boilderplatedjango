from django.shortcuts import render
from django.views.generic import TemplateView

from src.apps.whisper.main import NotificationService


# Create your views here.
class HomeView(TemplateView):
    template_name = 'website/index.html'
