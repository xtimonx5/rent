"""diploma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
from management.admin import admin_site
from django.conf.urls.static import static
from django.conf import settings
from management.views.index import index
from management.views.about import about
from management.views.cars import cars


urlpatterns = [
    # url(r'^grappelli/', include('grappelli.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', include(admin_site.urls)),
    url(r'^$', index, name='index'),
    url(r'^about/$', about, name='about'),
    url(r'^cars/$', cars, name='cars')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
              # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
