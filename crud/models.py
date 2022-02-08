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
    ratting = (
        (1, "Worst"),
        (2, "Bad"),
        (3, "Not Bad"),
        (4, "Good"),
        (5, "Excellent"),
    )
    num_stars = models.IntegerField(choices=ratting)
    def __str__(self):
        return self.name + ", Ratting: " + str(self.num_stars)

    class Meta:
        db_table = 'Album'