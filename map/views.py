from django.shortcuts import render
from .models import Config
from .models import QueryField

def map(request):
  config = Config.objects.order_by('-pub_date')[0]
  query_field_data = list(QueryField.objects.all())
  query_fields = []
  for query_field in query_field_data:
    if not query_field.enabled:
      continue
    query_field_id = str(query_field.query_field_id)
    query_field_type = str(query_field.query_field_type)
    query_field_name = str(query_field.query_field_name)
    query_field_label_eng = str(query_field.query_field_label_eng)
    query_field_label_esp = unicode(query_field.query_field_label_esp)
    data_sources = str(query_field.data_sources).replace('\n', ',').replace('\r', '')
    query_choices_vals = str(query_field.query_choices_vals).split('\n')#.replace('\n', ',').replace('\r', '') # name in XLS Form
    query_choices_labels_eng = str(query_field.query_choices_labels_eng).split('\n')#.replace('\n', ',').replace('\r', '') # label_english in XLS Form
    query_choices_labels_esp = unicode(query_field.query_choices_labels_esp).split('\n')#.replace('\n', ',').replace('\r', '') # label_espanol in XLS Form
    query_choices = []
    for i in range(len(query_choices_vals)):
      choice_obj = {
        'val': query_choices_vals[i],
        'label_eng': query_choices_labels_eng[i],
        'label_esp': query_choices_labels_esp[i]
      }
      query_choices.append(choice_obj)
    field_obj = {
      'id': query_field_id,
      'type': query_field_type,
      'name': query_field_name,
      'label_eng': query_field_label_eng,
      'label_esp': query_field_label_esp,
      'data_sources': data_sources,
      'choices': query_choices
    }
    query_fields.append(field_obj)
  context = {
    'config': config,
    'query_fields': query_fields
  }
  return render(request, 'map/map.html', context)
