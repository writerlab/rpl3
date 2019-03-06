from __future__ import unicode_literals
from django.db import models

class Kontak(models.Model):
  email = models.CharField(max_length=50)
  twitter = models.CharField(max_length=40, null=True)
  github = models.CharField(max_length=50)
  no_hp = models.CharField(max_length=13)

  def __unicode__(self):
    return self.email
