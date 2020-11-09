"""farmview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include(blog_urls))
"""
from django.urls import include, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^map/', include('map.urls')),
    re_path(r'^', include('pages.urls')),
    re_path(r'^weblog/', include('zinnia.urls')),
    re_path(r'^comments/', include('django_comments.urls')),
    re_path(r'^i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# blog_urls = ([
#     re_path(r'^', include('zinnia.urls.capabilities')),
#     re_path(r'^search/', include('zinnia.urls.search')),
#     re_path(r'^sitemap/', include('zinnia.urls.sitemap')),
#     re_path(r'^trackback/', include('zinnia.urls.trackback')),
#     re_path(r'^blog/tags/', include('zinnia.urls.tags')),
#     re_path(r'^blog/feeds/', include('zinnia.urls.feeds')),
#     re_path(r'^blog/random/', include('zinnia.urls.random')),
#     re_path(r'^blog/authors/', include('zinnia.urls.authors')),
#     re_path(r'^blog/categories/', include('zinnia.urls.categories')),
#     re_path(r'^blog/comments/', include('zinnia.urls.comments')),
#     re_path(r'^blog/', include('zinnia.urls.entries')),
#     re_path(r'^blog/', include('zinnia.urls.archives')),
#     re_path(r'^blog/', include('zinnia.urls.shortlink')),
#     re_path(r'^blog/', include('zinnia.urls.quick_entry'))
# ], 'zinnia')
