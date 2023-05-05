from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    contacts = models.CharField(max_length=11)
    address = models.CharField(max_length=70)
    status = models.CharField(max_length=70)