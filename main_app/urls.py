from django.urls import path
from . import views

#paths 
urlpatterns = [
    #path for the home page
    path('', views.Home.as_view(), name="home"),
    path('profile/', views.Profile.as_view(), name="users-profile"),
]