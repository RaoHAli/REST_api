from django.db import models
import datetime


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.datetime.now)


# class Group(models.Model):
#     name = models.CharField(max_length=100)
