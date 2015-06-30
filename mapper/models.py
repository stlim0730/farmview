from django.db import models

class AdminSetting(models.Model):
  vizjson_url = models.CharField(max_length=150)
  pub_date = models.DateTimeField(auto_now=True)
  optional_note = models.CharField(max_length=200)
  
  def __unicode__(self):
    return unicode(self.vizjson_url)
