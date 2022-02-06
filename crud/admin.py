from django.contrib import admin
from crud.models import Album, Musician

# Register your models here.
admin.site.register(Musician),
admin.site.register(Album)
