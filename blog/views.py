from __future__ import unicode_literals
from django.shortcuts import render
from blog.models import Artikel

# Create your views here.
def home(request):
  nama = "ZUL HILMI"
  buah = ['Apel', 'Anggur', 'Pear', 'Jeruk']
  return render(request, 'layout/index.html', {'nama':nama, 'buahbuahan':buah})

def about(request):
  return render(request, 'layout/about.html')

def kontak(request):
  return render(request, 'layout/kontak.html')

def blog(request):
  # select * from Artikel where publish=true
  blogs = Artikel.objects.filter(publish=True)
  return render(request, 'layout/blog.html', {'blogs':blogs})



