from django.conf.urls import url
from django.contrib import admin

from blog.views import *
from contact.views import contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^about/', about),
    url(r'^kontak/', contact),
    url(r'^blog/', blog),
]
