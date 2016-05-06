from django.contrib import admin
from rest_ngsi10.models import Subscription
from .models import Example

admin.site.register(Subscription)
admin.site.register(Example)
