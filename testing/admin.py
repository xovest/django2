from django.contrib import admin
from .models import Item, Something
# Register your models here.
admin.site.register(Something)
admin.site.register(Item)