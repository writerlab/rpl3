# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'layout/index.html')

def about(request):
  return render(request, 'layout/about.html')

def kontak(request):
  return render(request, 'layout/kontak.html')


def blog(request):
  return render(request, 'layout/blog.html')



