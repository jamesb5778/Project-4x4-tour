from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"


class Profile(View):

    def get(self, request):
        return HttpResponse("4x4 User Profile Page")