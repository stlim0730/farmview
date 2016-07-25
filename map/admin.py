from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Config
from .models import Datafield
from .models import FormData
import sys
sys.path.insert(0, '/farmview/farmview_geodata_processing')

class ConfigAdmin(admin.ModelAdmin):
  list_display = ('pub_date', 'vizjson_url', 'optional_note')

admin.site.register(Config, ConfigAdmin)

class DatafieldAdmin(admin.ModelAdmin):
  list_display = ('datafield_id', 'datafield_name', 'data_sources', 'datafield_type', 'use_for_query_ui', 'use_for_detail_popup', 'enabled')

admin.site.register(Datafield, DatafieldAdmin)

class FormDataAdmin(admin.ModelAdmin):
  list_display = ('formdata_id', 'ona_id', 'dropbox_url', 'last_synced_date', 'optional_note', 'button')
  def button(self, obj):
    return mark_safe('<input type="button" value="Force Sync">')

admin.site.register(FormData, FormDataAdmin)
