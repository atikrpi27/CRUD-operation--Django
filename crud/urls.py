from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

apps_name = 'crud'

urlpatterns = [
    path('', views.index, name='home'),
    path('musician/', views.musician, name='musician'),
    path('album/', views.album, name='album'),
    path('album-list/<int:artist_id>/', views.album_list, name='album-list'),
    path('edit-artist/<int:artist_id>/', views.edit_artist, name='edit-artist'),
]
