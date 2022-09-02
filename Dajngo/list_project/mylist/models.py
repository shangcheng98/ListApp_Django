from unicodedata import name
from django.db import models
from datetime import date

# Create your models here.
# extends models
class user(models.Model):
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200,default="123456")
    joinPoint = models.DateField(default=date.today)

class ListItem(models.Model):
    name = models.CharField(max_length=200)
    context = models.CharField(max_length=400)
    time = models.DateField(default=date.today)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.context