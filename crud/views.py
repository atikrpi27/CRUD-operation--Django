from django.shortcuts import render
from django.http import HttpResponse
from .models import Musician, Album
from . import form
# Create your views here.

def index(request):
    diction = {'title' : 'Home Page'}
    return render(request,'index.html', diction)

def musician(request):
    forms = form.MusicianForm()
    if request.method == "POST":
        forms = form.MusicianForm(request.POST)

        if forms.is_valid():
            forms.save(commit=True)
            return index(request)
            
    diction = {'title' : 'Musician List', 'musician_form' : forms}
    return render(request,'musician.html', diction)

def album(request):
    diction = {'title' : 'Album'}
    return render(request,'album.html', diction)