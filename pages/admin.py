from django.contrib import admin

from .models import Notice
from .models import AboutPage

admin.site.register(Notice)

admin.site.register(AboutPage)
