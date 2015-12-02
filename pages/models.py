from django.db import models

class Notice(models.Model):
  title = models.CharField(max_length=100, blank=True)
  content = models.TextField(blank=True)

  NOTICE_TYPE_DEFAULT = 'panel-default'
  NOTICE_TYPE_PRIMARY = 'panel-primary'
  NOTICE_TYPE_SUCCESS = 'panel-success'
  NOTICE_TYPE_WARNING = 'panel-warning'
  NOTICE_TYPE_DANGER = 'panel-danger'
  NOTICE_TYPE_INFO = 'panel-info'
  NOTICE_TYPE_CHOICES = (
      (NOTICE_TYPE_DEFAULT, 'Default'),
      (NOTICE_TYPE_PRIMARY, 'Primary'),
      (NOTICE_TYPE_SUCCESS, 'Success'),
      (NOTICE_TYPE_WARNING, 'Warning'),
      (NOTICE_TYPE_DANGER, 'Danger'),
      (NOTICE_TYPE_INFO, 'Info')
  )
  notice_type = models.CharField(max_length=13, choices=NOTICE_TYPE_CHOICES, default=NOTICE_TYPE_DEFAULT)

  def __unicode__(self):
    return unicode(self.title)

class AboutPage(models.Model):
  html = models.TextField(blank=True)

  def __unicode__(self):
    return unicode(self.html)
  