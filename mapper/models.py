from django.db import models

class AdminSetting(models.Model):
  vizjson_url = models.CharField(max_length=150)
  pub_date = models.DateTimeField(auto_now=True)
  optional_note = models.CharField(max_length=200)
  
  def __unicode__(self):
    return unicode(self.vizjson_url)
    
class SurveyQuestion(models.Model):
  id = models.IntegerField(primary_key=True)
  type = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  label_english = models.TextField()
  label_espanol = models.TextField()
  hint_english = models.TextField()
  hint_espanol = models.TextField()
  required = models.BooleanField()
  constraint = models.CharField(max_length=30)
  constraint_message = models.TextField()
  relevant = models.TextField()
  default = models.CharField(max_length=30)
  appearance = models.CharField(max_length=30)
  calculation = models.CharField(max_length=30)
  
  def __unicode__(self):
    return unicode(self.name)
