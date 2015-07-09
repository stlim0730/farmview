from django.db import models

class Config(models.Model):
  vizjson_url = models.CharField(max_length=150)
  pub_date = models.DateTimeField(auto_now=True)
  optional_note = models.CharField(max_length=200)
  
  def __unicode__(self):
    return unicode(self.vizjson_url)

class SurveyQuestion(models.Model):
  id = models.IntegerField(primary_key=True)
  type = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  label_english = models.TextField(blank=True)
  label_espanol = models.TextField(blank=True)
  hint_english = models.TextField(blank=True)
  hint_espanol = models.TextField(blank=True)
  required = models.BooleanField()
  constraint = models.CharField(max_length=30, blank=True)
  constraint_message = models.TextField(blank=True)
  relevant = models.TextField(blank=True)
  default = models.CharField(max_length=30, blank=True)
  appearance = models.CharField(max_length=30, blank=True)
  calculation = models.CharField(max_length=30, blank=True)
  queryable = models.BooleanField(default=False)
  
  def __unicode__(self):
    return unicode(self.name)

class SurveyChoice(models.Model):
  id = models.IntegerField(primary_key=True)
  question = models.ForeignKey(SurveyQuestion, to_field='id', null=True)
  list_name = models.CharField(max_length=30)
  name = models.CharField(max_length=30)
  label_english = models.TextField(blank=True)
  label_espanol = models.TextField(blank=True)
  image = models.CharField(max_length=30, blank=True)

  def __unicode__(self):
    return unicode(self.name)
