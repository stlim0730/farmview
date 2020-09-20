from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.map, name='map'),
    re_path(r'^geocode/(.*)$', views.geocode, name='geocode'),
    re_path(r'^datafields$', views.datafields, name='datafields'),
    re_path(r'^config$', views.config, name='config')
]
