from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Offroad_Park

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Profile(TemplateView):
    template_name = "profile.html"

class Offroad_Parks(TemplateView):
    template_name = "park-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["offroad_parks"] = Offroad_Park.objects.all()
        return context