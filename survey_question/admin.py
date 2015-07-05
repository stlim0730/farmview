from django.contrib import admin
from import_export import resources
from .models import SurveyQuestion
from import_export.admin import ImportExportModelAdmin

class SurveyQuestionResource(resources.ModelResource):
    class Meta:
        model = SurveyQuestion
        # fields = ('appearance', 'calculation', 'constraint', 'constraint_message', 'default', 'hint_english', 'hint_espanol', 'label_english', 'label_espanol', 'name', 'relevant', 'required', 'q_type')

class SurveyQuestionAdmin(ImportExportModelAdmin):
    resource_class = SurveyQuestionResource

admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
