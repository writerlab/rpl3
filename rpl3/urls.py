from django.conf.urls import url
from django.contrib import admin

from blog.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/', about),
    url(r'^kontak/', kontak),
    url(r'^blog/', blog),
]
