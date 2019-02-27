from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Kategori(models.Model):
  nama = models.CharField(max_length=20)
  keterangan = models.TextField(null=True)

  def __unicode__(self):
    return self.nama


class Artikel(models.Model):
  judul = models.CharField(max_length=50)
  tanggal = models.DateField()
  penulis = models.CharField(max_length=20)
  konten = models.TextField()
  publish = models.BooleanField(default=True)
  kategori = models.ForeignKey(Kategori, default=False)
  
  def __unicode__(self):
    return self.judul

