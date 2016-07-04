from django.shortcuts import render
from django.contrib.sitemaps import Sitemap

##
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext
##

def index(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')

def mapbook(request):
  from .models import Mapbook
  mapbooks = Mapbook.objects.order_by('-pub_date')
  context = {
    'mapbooks': mapbooks
  }
  return render(request, 'pages/mapbook.html', context)

def contact(request):
  return render(request, 'pages/contact.html')
