"""sitoweb_mlc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from mywebsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mywebsite/', views.mywebsite, name='homepage'),
    path('mywebsite/about', views.about, name='about'),
    path('mywebsite/skills', views.skills, name='skills'),
    path('mywebsite/education', views.education, name='education'),
    path('mywebsite/experience', views.experience, name='experience'),
    path('mywebsite/master', views.master, name='master'),
    path('mywebsite/contact', views.contact, name='contact'),
]
