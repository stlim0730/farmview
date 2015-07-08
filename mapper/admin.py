from django.contrib import admin
from import_export import resources
from .models import AdminSetting
from .models import SurveyQuestion
from import_export.admin import ImportExportModelAdmin

class AdminSettingMA(admin.ModelAdmin):
  list_display = ('pub_date', 'vizjson_url', 'optional_note')

admin.site.register(AdminSetting, AdminSettingMA)

class SurveyQuestionResource(resources.ModelResource):
  class Meta:
    model = SurveyQuestion

def make_queryable(modeladmin, request, queryset):
    queryset.update(queryable=True)
make_queryable.short_description = 'Mark selected fields as queryable'

def make_not_queryable(modeladmin, request, queryset):
    queryset.update(queryable=False)
make_not_queryable.short_description = 'Mark selected fields as NOT queryable'


class SurveyQuestionAdmin(ImportExportModelAdmin):
  resource_class = SurveyQuestionResource
  list_display = ('id', 'name', 'type', 'queryable', 'label_english')
  actions = [make_queryable, make_not_queryable]

admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
