from django.contrib import admin

# Register your models here.
from .models import Item, Supplier

admin.site.register(Supplier)
admin.site.register(Item)
