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
