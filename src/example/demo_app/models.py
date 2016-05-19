from __future__ import unicode_literals

from django.db import models
from datetime import datetime


class Example(models.Model):
    # attribute examples - an integer field and a char field
    name = models.CharField(max_length=200)
    uuid = models.IntegerField()
    parking_spot = models.IntegerField()
    is_available = models.BooleanField()
    asset = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now)


class AnotherExample(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.IntegerField()
    parking_spot = models.IntegerField()
    is_available = models.BooleanField()
    asset = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=datetime.now)