from re import A
from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician, Album
from . import form
# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')
    diction = {'title' : 'Home Page', 'musician_list' : musician_list}
    return render(request,'index.html', diction)

def musician(request):
    forms = form.MusicianForm()
    if request.method == "POST":
        forms = form.MusicianForm(request.POST)

        if forms.is_valid():
            forms.save(commit=True)
            return index(request)
            
    diction = {'title' : 'Musician Form', 'musician_form' : forms}
    return render(request,'musician.html', diction)

def album(request):
    forms = form.AlbumForm()
    if request.method == "POST":
        forms = form.AlbumForm(request.POST)

        if forms.is_valid():
            forms.save(commit = True)
            return index(request)

    diction = {'title' : 'Album Form', 'album_form': forms}
    return render(request,'album.html', diction)


def album_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    diction = {'title' : 'Album List: ', 'artist_info': artist_info}
    return render(request, 'album_list.html', diction)