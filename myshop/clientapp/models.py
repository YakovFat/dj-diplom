from django.db import models
from django.contrib.auth.models import User


class Phone(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.SlugField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.ManyToManyField('Phone')