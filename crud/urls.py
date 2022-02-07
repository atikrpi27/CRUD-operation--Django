from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

apps_name = 'crud'

urlpatterns = [
    path('', views.index, name='home'),
    path('musician/', views.musician, name='musician'),
    path('album/', views.album, name='album'),
]
