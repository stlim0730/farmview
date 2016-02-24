from django.db import models
from django.utils.text import slugify

class Mapbook(models.Model):
  mapbook_id = models.AutoField(primary_key = True)
  title = models.CharField(max_length = 100, unique = True)
  title_short = models.CharField(max_length = 100, default = '', unique = True)
  slug = models.SlugField(max_length = 100, editable = False)
  pub_date = models.DateTimeField(auto_now = True)
  thumbnail_url = models.CharField(max_length = 100, unique = True)
  text = models.TextField(blank = True)
  enabled = models.BooleanField(default = True)
  optional_note = models.CharField(max_length = 200, blank = True)
  
  def __unicode__(self):
    return unicode(self.slug)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title_short)
    super(Mapbook, self).save(*args, **kwargs)
