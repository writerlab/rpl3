from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("halo ini halaman depan...")

def about(request):
    return HttpResponse('ini halaman ABOUT: ZUL HILMI')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^about/', about),
]
