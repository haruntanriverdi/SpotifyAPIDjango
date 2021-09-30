from django.urls import path
from django.conf.urls import url
from track import views

from . import views


urlpatterns = [
    path('', views.HomeView, name = 'home'),
    path('track/<str:genre>/', views.TrackView, name='track'),

]
