from django.urls import path
from . import views

#paths 
urlpatterns = [
    #path for the home page
    path('', views.Home.as_view(), name="home"),
    #path for the profile page
    path('profile/', views.Profile.as_view(), name="profile"),
    #path for the offroad parks list page
    path('park-list/', views.Offroad_Parks.as_view(), name='parks-list'),
    #path to add a offroad park
    path('offroadpark/new/', views.AddOffroadPark.as_view(), name='new-offroad-park'),
]
