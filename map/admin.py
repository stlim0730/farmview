from django.contrib import admin
from .models import Config
from .models import Datafield

class ConfigAdmin(admin.ModelAdmin):
  list_display = ('pub_date', 'vizjson_url', 'optional_note')

admin.site.register(Config, ConfigAdmin)

class DatafieldAdmin(admin.ModelAdmin):
  list_display = ('datafield_id', 'datafield_name', 'data_sources', 'datafield_type', 'use_for_query_ui', 'use_for_detail_popup', 'enabled')

admin.site.register(Datafield, DatafieldAdmin)
