from django.shortcuts import render
from .models import Notice
from .models import AboutPage

def index(request):
  notices = list(Notice.objects.all())
  context = { 'notices': notices }
  return render(request, 'pages/index.html', context)

def about(request):
  about_page = list(AboutPage.objects.all())[-1]
  context = { 'about_page': about_page }
  # context = { 'about_page': 'asdfsa' }
  return render(request, 'pages/about.html', context)
