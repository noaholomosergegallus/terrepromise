from django.contrib import admin

# Register your models here.
from .models import Articles, Category
admin.site.register(Articles)
admin.site.register(Category)

