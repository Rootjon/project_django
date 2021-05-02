from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max_length=30)
    address = models.TextField()
    image = models.ImageField()