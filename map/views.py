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
  # for survey_question in survey_questions:
  #   queryable = survey_question.queryable
  #   if not queryable:
  #     continue
  #   q_id = survey_question.id
  #   q_type = survey_question.type
  #   q_name = survey_question.name
  #   q_obj = {
  #     'q_id': str(q_id),
  #     'q_type': str(q_type),
  #     'q_name': str(q_name)
  #   }
  #   q_data.append(q_obj)
  #   choices = list(SurveyChoice.objects.filter(question=q_id))
  #   if len(choices) > 0:
  #     q_obj['choices'] = []
  #   for choice in choices:
  #     c_id = choice.id
  #     q_name = choice.question
  #     c_list_name = choice.list_name
  #     c_name = choice.name
  #     c_label_english = choice.label_english
  #     c_label_espanol = choice.label_espanol
  #     c_obj = {
  #       'c_id': str(c_id),
  #       'q_name': str(q_name),
  #       'c_list_name': str(c_list_name),
  #       'c_name': str(c_name),
  #       'c_label_english': str(c_label_english),
  #       'c_label_espanol': unicode(c_label_espanol)
  #     }
  #     # c_data.append(c_obj)
  #     q_obj['choices'].append(c_obj)
  # context = {
  #   'config': config,
  #   # 'q_data': q_data
  #   'q_data': [
  #     {
  #       'q_id': '0',
  #       'q_type': 'integer',
  #       'q_name': 'apn',
  #       'data_source': 'central_coast_joined',
  #       'choices': []
  #     },
  #     {
  #       'q_id': '1',
  #       'q_type': 'text',
  #       'q_name': 'area',
  #       'data_source': 'central_coast_joined',
  #       'choices': []
  #     },
  #     {
  #       'q_id': '2',
  #       'q_type': 'text',
  #       'q_name': 'survey_ranch_details_lease_rate_current',
  #       'choices': []
  #     },
  #     {
  #       'q_id': '3',
  #       'q_type': 'select_one',
  #       'q_name': 'survey_land_availability',
  #       'choices': [
  #         {
  #           'c_id': '0',
  #           'q_name': 'survey_land_availability',
  #           'c_list_name': 'survey_land_availability',
  #           'c_name': 'no_land_availalble',
  #           'c_label_english': 'The property isn\'t available',
  #           'c_label_espanol': u'Ningun parte de la parcela esta disponible'
  #         },
  #         {
  #           'c_id': '1',
  #           'q_name': 'survey_land_availability',
  #           'c_list_name': 'survey_land_availability',
  #           'c_name': 'part_of_farm_available',
  #           'c_label_english': 'Part of the property is available',
  #           'c_label_espanol': u'Parte de la parcela esta disponible'
  #         },
  #         {
  #           'c_id': '2',
  #           'q_name': 'survey_land_availability',
  #           'c_list_name': 'survey_land_availability',
  #           'c_name': 'whole_farm_available',
  #           'c_label_english': 'The whole property is available',
  #           'c_label_espanol': u'La parcela entera esta disponible'
  #         }
  #       ]
  #     }
  #   ]
  # }
  return render(request, 'map/map.html', context)
