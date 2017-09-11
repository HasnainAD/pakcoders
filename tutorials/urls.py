
from django.conf.urls import url, include

from . import views

'''AUTHOR : PAKISARUS'''


patterns =[url(r'^$', views.detail,name='detail', ),
           url(r'^(?P<articlename>\w+)/', views.detail, name='detail'),]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<tutname>python)/', include(patterns)),
    url(r'^(?P<tutname>java)/', include(patterns)),
    url(r'^(?P<tutname>csharp)/', include(patterns)),
]