from django.urls import path
from . import views

#paths 
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
]