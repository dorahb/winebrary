from django.contrib import admin

# Register your models here.

from .models import Book, Profile

admin.site.register(Profile)
admin.site.register(Book)
