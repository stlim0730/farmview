from django.shortcuts import render
from .models import AdminSetting

def index(request):
  admin_setting = AdminSetting.objects.order_by('-pub_date')[0]
  context = {
    'admin_setting': admin_setting
  }
  return render(request, 'mapper/index.html', context)
