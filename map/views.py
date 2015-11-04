from django.shortcuts import render
from .models import Config
from .models import SurveyQuestion
from .models import SurveyChoice

def map(request):
  config = Config.objects.order_by('-pub_date')[0]
  survey_questions = list(SurveyQuestion.objects.all())
  q_data = []
  c_data = []
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
  context = {
    'config': config,
    # 'q_data': q_data
    'q_data': [
      {
        'q_id': '0',
        'q_type': 'integer',
        'q_name': 'apn',
        'data_source': 'central_coast_joined',
        'choices': []
      },
      {
        'q_id': '1',
        'q_type': 'text',
        'q_name': 'area',
        'data_source': 'central_coast_joined',
        'choices': []
      },
      {
        'q_id': '2',
        'q_type': 'text',
        'q_name': 'survey_ranch_details_lease_rate_current',
        'choices': []
      },
      {
        'q_id': '3',
        'q_type': 'select_one',
        'q_name': 'survey_land_availability',
        'choices': [
          {
            'c_id': '0',
            'q_name': 'survey_land_availability',
            'c_list_name': 'survey_land_availability',
            'c_name': 'no_land_availalble',
            'c_label_english': 'The property isn\'t available',
            'c_label_espanol': u'Ningun parte de la parcela esta disponible'
          },
          {
            'c_id': '1',
            'q_name': 'survey_land_availability',
            'c_list_name': 'survey_land_availability',
            'c_name': 'part_of_farm_available',
            'c_label_english': 'Part of the property is available',
            'c_label_espanol': u'Parte de la parcela esta disponible'
          },
          {
            'c_id': '2',
            'q_name': 'survey_land_availability',
            'c_list_name': 'survey_land_availability',
            'c_name': 'whole_farm_available',
            'c_label_english': 'The whole property is available',
            'c_label_espanol': u'La parcela entera esta disponible'
          }
        ]
      }
    ]
  }
  return render(request, 'map/map.html', context)
