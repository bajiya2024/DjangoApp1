from django.db import models

# Create your models here.

class Movie(models.Model):
    actor1 = models.CharField(max_length=30, default="dharmendra")
    actor_movie1 = models.CharField(max_length=50, default="some")
    genre1 = models.CharField(max_length=20, default=True)
    movie_logo1 = models.CharField(max_length=100, default=True)
class Song(models.Model):
    movie1 = models.ForeignKey(Movie, on_delete=models.CASCADE, default=True)
    file_type1 = models.CharField(max_length=50, default=True)
    song_name1 = models.CharField(max_length=100, default=True)
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summery = models.CharField(max_length=200)
