from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Config
from .models import Datafield
from .models import FormData
import os, requests
from farmview_geodata_processing.api_process import download_ona_data,upload_dropbox

class ConfigAdmin(admin.ModelAdmin):
  list_display = ('pub_date', 'vizjson_url', 'optional_note')

admin.site.register(Config, ConfigAdmin)

class DatafieldAdmin(admin.ModelAdmin):
  list_display = ('datafield_id', 'datafield_name', 'data_sources', 'datafield_type', 'use_for_query_ui', 'use_for_detail_popup', 'enabled')

admin.site.register(Datafield, DatafieldAdmin)

class FormDataAdmin(admin.ModelAdmin):
  list_display = ('formdata_id', 'import_id', 'ona_id', 'current', 'dropbox_url', 'last_synced_date', 'optional_note')
  exclude = ('import_id', 'dropbox_url')

  # call force sync on updated datasets
  def make_force_sync(modeladmin, request, queryset):
      for formdatas in queryset.all():
          download_ona_data(formdatas.ona_id)
          upload_dropbox('data_point.geojson','data_polygon.geojson')
          import_ids = filter(None, formdatas.import_id.split(","))
          for import_id in import_ids:
              url = 'https://calo1.cartodb.com/api/v1/synchronizations/' + import_id + '/sync_now?api_key=' + os.environ.get('CARTODB_API_KEY')
              header = {'Content-Length':0}
              res = requests.put(url, headers=header)
  actions = [make_force_sync]

admin.site.register(FormData, FormDataAdmin)
