"""
URL configuration for holamundo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views   

urlpatterns = [
    #está definiendo que el directorio raiz irá a la función home definida en el archivo urls.py de la aplicación core
    path('', views.home, name='home'),  
    path('portfolio/', views.portfolio, name='portfolio'),
    path('base/', views.base, name='base'),
    path('galeria/', views.galeria, name='galeria'),
    path('procedimiento/', views.procedimiento, name='procedimiento'),
    path('somos/', views.somos, name='somos'),
    path('ubicacion/', views.ubicacion, name='ubicacion'),
    path('admin/', admin.site.urls),
]
