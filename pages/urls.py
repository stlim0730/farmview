from django.urls import re_path

from pages import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^mapbook/$', views.mapbook, name='mapbook'),
    re_path(r'^contact/$', views.contact, name='contact')
]
