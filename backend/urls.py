"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.views.generic import TemplateView
from django.urls import include, path
from accounts.views import UserCreate

urlpatterns = [
    url(r'^$', UserCreate.as_view(), name='account-create'),
     path('admin/', admin.site.urls),
    path('api/', include('teams.urls')),
  # I think this is what was causing the NoReverseMatch error?  
  # url(r'^users/', include('accounts.urls')),
    url(r'^/', include('accounts.urls')),

    path('.*', TemplateView.as_view(template_name='index.html')),

]






"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('teams.urls')),
  # I think this is what was causing the NoReverseMatch error?  
  # url(r'^users/', include('accounts.urls')),
    url(r'^/', include('accounts.urls')),

    url('.*', TemplateView.as_view(template_name='index.html')),
]
"""
