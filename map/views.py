from django.shortcuts import render
import simplejson as json
from .models import Config
from .models import Datafield

def map(request):
  config = Config.objects.order_by('-pub_date')[0]
  datafield_data = list(Datafield.objects.all())
  datafields = []
  for query_field in datafield_data:
    if not query_field.enabled:
      continue
    datafield_id = str(query_field.datafield_id)
    datafield_type = str(query_field.datafield_type)
    datafield_name = str(query_field.datafield_name).strip()
    datafield_label_eng = str(query_field.datafield_label_eng)
    datafield_label_esp = unicode(query_field.datafield_label_esp)
    data_sources = str(query_field.data_sources).replace('\n', ',').replace('\r', '')
    query_choices_vals = str(query_field.query_choices_vals).split('\n')#.replace('\n', ',').replace('\r', '') # name in XLS Form
    query_choices_labels_eng = str(query_field.query_choices_labels_eng).split('\n')#.replace('\n', ',').replace('\r', '') # label_english in XLS Form
    query_choices_labels_esp = unicode(query_field.query_choices_labels_esp).split('\n')#.replace('\n', ',').replace('\r', '') # label_espanol in XLS Form
    query_choices = []
    if len(query_choices_vals) == len(query_choices_labels_eng):
      for i in range(len(query_choices_vals)):
        choice_obj = {
          'val': query_choices_vals[i].strip().replace('\r', ''),
          'label_eng': query_choices_labels_eng[i].replace('\r', '')
        }
        if len(query_choices_labels_esp) >= i + 1:
          choice_obj['label_esp'] = query_choices_labels_esp[i]
        query_choices.append(choice_obj)
    use_for_query_ui = query_field.use_for_query_ui
    use_for_detail_popup = query_field.use_for_detail_popup
    datafield_obj = {
      'id': datafield_id,
      'type': datafield_type,
      'name': datafield_name,
      'label_eng': datafield_label_eng,
      'label_esp': datafield_label_esp,
      'data_sources': data_sources,
      'choices': json.dumps(query_choices, separators=(',', ':'), sort_keys=True),
      'use_for_query_ui': use_for_query_ui,
      'use_for_detail_popup': use_for_detail_popup
    }
    datafields.append(datafield_obj)
  context = {
    'config': config,
    'datafields': datafields,
    'data_sources': ['central_coast_joined', 'data_point', 'data_polygon']
  }
  return render(request, 'map/map.html', context)
