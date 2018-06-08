from django.contrib import admin
from .models import Restaurant, Dish

class RAdmin(admin.ModelAdmin):
    list_display = ('name', 'town', 'state')

admin.site.register(Restaurant, RAdmin)
admin.site.register(Dish)
