from re import template
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
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

class AddOffroadPark(CreateView):
    model = Offroad_Park
    fields = ['name', 'location', 'state', 'image', 'Difficulty', 'Duration', 'Description', 'open_verified']
    template_name = "new-offroad-park.html"
    success_url = "/park-list/"

class OffroadParkDetail(DetailView):
    model = Offroad_Park
    template_name = "offroad-park-detail.html"