from django.shortcuts import render
from .models import AdminSetting

def index(request):
  admin_settings = AdminSetting.objects.order_by('-pub_date')[0]
  context = {
    'admin_settings': admin_settings
  }
  return render(request, 'mapper/index.html', context)
