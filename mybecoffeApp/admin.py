from django.contrib import admin

from mybecoffeApp.models import  users
from mybecoffeApp.models import presence
from mybecoffeApp.models import recettes

# Register your models here.

admin.site.register(users)
admin.site.register(presence)
admin.site.register(recettes)

