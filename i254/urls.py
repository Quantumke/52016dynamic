"""i254 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from app import  views
from i254 import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^portfolio/', views.portfolio_items, name='portfolio'),
    url(r'^prices/', views.pricelist, name='pricelist'),
    url(r'^requestquote/', views.quote, name='requestquote'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^images/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

