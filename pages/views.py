from django.shortcuts import render
from django.contrib.sitemaps import Sitemap

def index(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')

def mapbook(request):
  return render(request, 'pages/mapbook.html')

def contact(request):
  return render(request, 'pages/contact.html')
