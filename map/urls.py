from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.map, name='map'),
    url(r'^geocode/(.*)$', views.geocode, name='geocode'),
    url(r'^report/(.*)/(.*)$', views.gen_pdf, name='gen_pdf')    
]
