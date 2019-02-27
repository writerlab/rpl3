from __future__ import unicode_literals
from django.shortcuts import render

from .models import Contact


def contact(request):
  contacts = Contact.objects.all()
  return render(request, 'layout/kontak.html', {'contacts':contacts})
