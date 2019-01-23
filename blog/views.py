# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("halo ini halaman depan...")

def about(request):
    return HttpResponse('ini halaman ABOUT: ZUL HILMI')

def kontak(request):
  return HttpResponse('<h3>twitter: @hilmizul</h3>')



