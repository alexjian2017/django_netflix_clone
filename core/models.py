from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('ALL','ALL'),
    ('Kids','Kids'),
)

MOVIE_CHOICES= (
    ('seasonal','Seasonal'),
    ('single',"Single")
)
# Create your models here.
class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    name = models.CharField(max_length =255)
    age_limit = models.CharField(max_length =10,choices = AGE_CHOICES)
    uuid = models.UUIDField(default = uuid.uuid4)

class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    uuid = models.UUIDField(default = uuid.uuid4)
    type = models.CharField(max_length = 10, choices = MOVIE_CHOICES)
    videos = models.ManyToManyField('Videos')
    flyer = models.ImageField(upload_to = 'flyer')
    age_limit = models.CharField(max_length = 10, choices = AGE_CHOICES)


class Videos(models.Model):
    title = models.CharField(max_length = 255,null = True, blank=True)
    file = models.FileField(upload_to= 'movies')