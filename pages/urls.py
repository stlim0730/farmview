from django.conf.urls import url

from pages import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^mapbook/$', views.mapbook, name='mapbook'),
    url(r'^contact/$', views.contact, name='contact')
]
