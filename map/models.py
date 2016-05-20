from django.db import models

class Config(models.Model):
  vizjson_url = models.CharField(max_length=150)
  pub_date = models.DateTimeField(auto_now=True)
  optional_note = models.CharField(max_length=200, blank=True)
  
  def __unicode__(self):
    return unicode(self.vizjson_url)

class Datafield(models.Model):
  datafield_id = models.AutoField(primary_key = True)
  DATAFIELD_TYPE_CHOICES = (
                              ('text', 'Text'),
                              ('range', 'Range'),
                              ('select_one', 'Select One'),
                              ('select_multiple', 'Select Multiple')
                             )
  datafield_type = models.CharField(max_length = 20, choices=DATAFIELD_TYPE_CHOICES)
  datafield_name = models.CharField(max_length = 60)
  datafield_label_eng = models.CharField(max_length = 30, blank = False)
  datafield_label_esp = models.CharField(max_length = 30, blank = True)
  data_sources = models.TextField(blank = False)
  enabled = models.BooleanField(default = True)
  query_choices_vals = models.TextField(blank = True) # name in XLS Form
  query_choices_labels_eng = models.TextField(blank = True) # label_english in XLS Form
  query_choices_labels_esp = models.TextField(blank = True) # label_espanol in XLS Form
  use_for_query_ui = models.BooleanField(default = False)
  use_for_detail_popup = models.BooleanField(default = True)

  def __unicode__(self):
    return unicode(self.datafield_name)
