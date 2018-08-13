from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.map, name='map'),
    url(r'^geocode/(.*)$', views.geocode, name='geocode'),
    url(r'^datafields$', views.datafields, name='datafields'),
    url(r'^config$', views.config, name='config')
]
