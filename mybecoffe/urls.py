"""mybecoffe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from mybecoffeApp.views import create_arrival,update_depart, home,create_recettes, create_user, index_recettes, index_login, index_profile, index_users,logout_view,index_presences,update_recettes,destroy_recettes







urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('arrival/',create_arrival,name='arrival'),
    path('depart/',update_depart,name='depart'),
    path('recettes/', index_recettes,name='recettes'),
    path('recettes_form/',create_recettes,name='recettes_form'),
    path('recettes_form/<str:pk>',update_recettes,name='recettes_form_update'),
    path('recettes_delete/<str:pk>',destroy_recettes,name='recettes_delete'),
    path('register/',create_user,name='register'),
    path('login/',index_login,name='login'),
    path('logout/',logout_view,name='logout'),
    path('presences/',index_presences,name='presences'),
    path('profile/<int:pk>',index_profile,name='profile'),
    path('users/',index_users,name='users')
]
