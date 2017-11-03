from django.contrib import admin
from .models import Category,Tag,post

# Register your models here.

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(post)

