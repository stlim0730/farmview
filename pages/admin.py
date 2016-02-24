from django.contrib import admin
from .models import Mapbook

class MapbookAdmin(admin.ModelAdmin):
  list_display = ('title', 'pub_date')

admin.site.register(Mapbook, MapbookAdmin)
