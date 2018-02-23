"""myproject URL Configuration

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
from django.urls import path,include
from django.contrib.auth import views as auth_views
from myapp import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('person/', views.ListPersonView.as_view(), name='person'),
    path('admin/', admin.site.urls, name="admin"),
    path('create/', views.CreatePersonView.as_view(), name='person'),
    path('carcreate/', views.CreateCarView.as_view(), name='car'),
    path('rentcreate/', views.CreateRentView.as_view(), name='rent'),
    path('list/', views.list, name='list'),
    path('login/', auth_views.LoginView.as_view()),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('carlist/',views.CarListView.as_view(), name='carlist'),
    path('rentlist/',views.RentListView.as_view(), name='rentlist'),
]
