from django.shortcuts import render
from .models import Config
from .models import SurveyQuestion

def index(request):
  admin_settings = Config.objects.order_by('-pub_date')[0]
  survey_questions = list(SurveyQuestion.objects.all())
  query_fields = []
  for survey_question in survey_questions:
    queryable = survey_question.queryable
    if not queryable:
      continue
    type = survey_question.type
    name = survey_question.name
    field = {
      'type': str(type),
      'name': str(name)
    }
    query_fields.append(field)
  context = {
    'admin_settings': admin_settings,
    'query_fields': query_fields
  }
  return render(request, 'mapper/index.html', context)
