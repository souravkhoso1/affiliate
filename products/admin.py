from django.contrib import admin
from .models import Product, Department, Tag

# Register your models here.

admin.site.register(Product)
admin.site.register(Department)
admin.site.register(Tag)
