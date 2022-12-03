from django.contrib import admin

from .models import Cat # use .models b/c on same line as admin.py

# Register your models here.
admin.site.register(Cat) # this same line is how you would register any model

