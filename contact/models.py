from __future__ import unicode_literals
from django.db import models

class Contact(models.Model):
  email = models.CharField(max_length=50)
  twitter = models.CharField(max_length=50)
  github = models.CharField(max_length=60)
  no_hp = models.IntegerField()

  def __unicode__(self):
    return self.email