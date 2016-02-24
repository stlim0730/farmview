from django.db import models

class Mapbook(models.Model):
  mapbook_id = models.AutoField(primary_key = True)
  title = models.CharField(max_length = 80, unique = True)
  slug = models.SlugField(max_length = 80, editable = False)
  pub_date = models.DateTimeField(auto_now = True)
  thumbnail_url = models.CharField(max_length = 50, unique = True)
  text = models.TextField(blank = True)
  enabled = models.BooleanField(default = True)
  optional_note = models.CharField(max_length = 200, blank = True)
  
  def __unicode__(self):
    return unicode(self.slug)

  def save(self, *args, **kwargs):
    self.slug = slugify(self.title)
    super(Mapbook, self).save(*args, **kwargs)
