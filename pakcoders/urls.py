
from django.conf.urls import url, include
from django.contrib import admin

'''AUTHOR : PAKISARUS'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tuts/', include('tutorials.urls')),
]
