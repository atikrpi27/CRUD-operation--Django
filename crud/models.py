from tkinter import CASCADE
from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name + " , " + self.instrument

    class Meta:
        db_table = 'Musician'

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    release_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Album'