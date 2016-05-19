from django.contrib import admin
from rest_ngsi10.models import Subscription
from .models import Example, AnotherExample

admin.site.register(AnotherExample)
admin.site.register(Example)
