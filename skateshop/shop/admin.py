from django.contrib import admin


# Register your models here.
from .models import Shop, Category, Sub_Category

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Sub_Category)
