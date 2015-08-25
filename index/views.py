from django.shortcuts import render
from .models import Notice

def index(request):
  notices = list(Notice.objects.all())
  context = { 'notices': notices }
  return render(request, 'index/index.html', context)
