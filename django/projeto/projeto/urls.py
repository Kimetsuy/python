"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
#C:/Users/Administrador/AppData/Local/Python/pythoncore-3.14-64/python.exe c:\Users\Administrador\Desktop\backup\programaçao\python\python\django\projeto\manage.py runserver

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),#a url vazia '' é a pagina inicial,
    path('teste/', include('teste.urls')),
]