from django.db import models

class Config(models.Model):
  vizjson_url = models.CharField(max_length=150)
  pub_date = models.DateTimeField(auto_now=True)
  optional_note = models.CharField(max_length=200, blank=True)
  
  def __unicode__(self):
    return unicode(self.vizjson_url)

class QueryField(models.Model):
  query_field_id = models.AutoField(primary_key = True)
  query_field_type = models.CharField(max_length = 20)
  query_field_name = models.CharField(max_length = 30)
  query_field_label_eng = models.CharField(max_length = 30, blank = False)
  query_field_label_esp = models.CharField(max_length = 30, blank = True)
  data_sources = models.TextField(blank = False)
  enabled = models.BooleanField(default = True)
  query_choices_vals = models.TextField(blank = True) # name in XLS Form
  query_choices_labels_eng = models.TextField(blank = True) # label_english in XLS Form
  query_choices_labels_esp = models.TextField(blank = True) # label_espanol in XLS Form
  
  def __unicode__(self):
    return unicode(self.query_field_name)

# class QueryChoice(models.Model):
#   query_choice_id = models.IntegerField(primary_key = True)
#   query_field_id = models.ForeignKey(QueryField, to_field = 'query_field_id', null = False)
#   query_choice_name = models.CharField(max_length = 30) # list_name in XLS Form
#   query_choices_vals = models.TextField(blank = False) # name in XLS Form
#   query_choices_labels_eng = models.TextField(blank = False) # label_english in XLS Form
#   query_choices_labels_esp = models.TextField(blank = True) # label_espanol in XLS Form

#   def __unicode__(self):
#     return unicode(self.name)

# class SurveyQuestion(models.Model):
#   id = models.IntegerField(primary_key=True)
#   type = models.CharField(max_length=30)
#   name = models.CharField(max_length=30)
#   label_english = models.TextField(blank=True)
#   label_espanol = models.TextField(blank=True)
#   hint_english = models.TextField(blank=True)
#   hint_espanol = models.TextField(blank=True)
#   required = models.BooleanField()
#   constraint = models.CharField(max_length=30, blank=True)
#   constraint_message = models.TextField(blank=True)
#   relevant = models.TextField(blank=True)
#   default = models.CharField(max_length=30, blank=True)
#   appearance = models.CharField(max_length=30, blank=True)
#   calculation = models.CharField(max_length=30, blank=True)
#   queryable = models.BooleanField(default=False)
  
#   def __unicode__(self):
#     return unicode(self.name)

# class SurveyChoice(models.Model):
#   id = models.IntegerField(primary_key=True)
#   question = models.ForeignKey(SurveyQuestion, to_field='id', null=True)
#   list_name = models.CharField(max_length=30)
#   name = models.CharField(max_length=30)
#   label_english = models.TextField(blank=True)
#   label_espanol = models.TextField(blank=True)
#   image = models.CharField(max_length=30, blank=True)

#   def __unicode__(self):
#     return unicode(self.name)
