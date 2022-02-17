from re import A
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician, Album
from . import form
from django.db.models import Avg
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
    album_list = Album.objects.filter(artist=artist_id).order_by('name')
    artist_ratting = Album.objects.filter(artist=artist_id).aggregate(Avg('num_stars'))

    diction = {'title' : 'Album List: ', 'artist_info': artist_info, 'album_list': album_list, 'artist_ratting':artist_ratting}
    return render(request, 'album_list.html', diction)
    


def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    forms = form.MusicianForm(instance=artist_info)
    
    if request.method == "POST":
        forms = form.MusicianForm(request.POST, instance = artist_info)

        if forms.is_valid():
            forms.save(commit = True)
            return album_list(request, artist_id)

    diction = {'edit_artist':forms}
    return render(request,'edit_artist.html', diction)


def album_lists(request):
    return render(request,'album_list.html')

def edit_album(request,album_id):
    album_info = Album.objects.get(pk=album_id)
    forms = form.AlbumForm(instance = album_info)
    diction = {}

    if request.method == "POST":
        forms = form.AlbumForm(request.POST, instance = album_info)

        if forms.is_valid():
            forms.save(commit = True)
            diction.update({'success_text':'Succesfully Updated!'})

    diction.update({'edit_album':forms})
    return render(request,'edit_album.html', diction)