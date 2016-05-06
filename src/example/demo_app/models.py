from __future__ import unicode_literals

from django.db import models


class Example(models.Model):
    # attribute examples - an integer field and a char field
    attribute1 = models.IntegerField()
    attribute2 = models.CharField(max_length=20)
