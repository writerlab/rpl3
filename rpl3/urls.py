from django.conf.urls import url
from django.contrib import admin

from blog.views import *
from kontak.views import tampilkan_kontak

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/', about),
    url(r'^blog/', blog),
    url(r'^kontak/', tampilkan_kontak),
]
