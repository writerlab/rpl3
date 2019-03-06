from __future__ import unicode_literals
from django.shortcuts import render
from kontak.models import Kontak

def tampilkan_kontak(request):
  # select * from Kontak
  data_kontak = Kontak.objects.all()
  return render(request, 'layout/kontak.html', {'data_kontak':data_kontak})

