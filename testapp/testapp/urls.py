"""testapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path('', demo),
    path('table/', datatables, name="table"),
    path('calendar/', calendar , name="calendar"),
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('admin/ajax/', include('grappelli_extras.ajax_urls')),
    path('admin/extras/', include('grappelli_extras.extras_urls')),
    path('admin/', admin.site.urls),
]
