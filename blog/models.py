from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Artikel(models.Model):
  judul = models.CharField(max_length=50)
  tanggal = models.DateField()
  penulis = models.CharField(max_length=20)
  konten = models.TextField()
  
  def __unicode__(self):
    return self.judul

