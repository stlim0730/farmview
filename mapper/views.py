from django.shortcuts import render
from .models import Config
from .models import SurveyQuestion
from .models import SurveyChoice
from django.core import serializers

def index(request):
  config = Config.objects.order_by('-pub_date')[0]
  survey_questions = list(SurveyQuestion.objects.all())
  q_data = []
  c_data = []
  for survey_question in survey_questions:
    queryable = survey_question.queryable
    if not queryable:
      continue
    q_id = survey_question.id
    q_type = survey_question.type
    q_name = survey_question.name
    q_obj = {
      'q_id': str(q_id),
      'q_type': str(q_type),
      'q_name': str(q_name)
    }
    q_data.append(q_obj)
    choices = list(SurveyChoice.objects.filter(question=q_id))
    for choice in choices:
      c_id = choice.id
      q_name = choice.question
      c_list_name = choice.list_name
      c_name = choice.name
      c_label_english = choice.label_english
      c_label_espanol = choice.label_espanol
      c_obj = {
        'c_id': str(c_id),
        'q_name': str(q_name),
        'c_list_name': str(c_list_name),
        'c_name': str(c_name),
        'c_label_english': str(c_label_english),
        'c_label_espanol': unicode(c_label_espanol)
      }
      c_data.append(c_obj)
  context = {
    'config': config,
    'q_data': q_data,
    'c_data': c_data
  }
  return render(request, 'mapper/index.html', context)
