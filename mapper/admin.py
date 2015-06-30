from django.contrib import admin
from .models import AdminSetting

class AdminSettingMA(admin.ModelAdmin):
  list_display = ('pub_date', 'vizjson_url', 'optional_note')
  
admin.site.register(AdminSetting, AdminSettingMA)
