from __future__ import unicode_literals
from django.contrib import admin

from blog.models import Artikel, Kategori

# Register your models here.
admin.site.register(Artikel)
admin.site.register(Kategori)
