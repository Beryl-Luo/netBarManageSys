"""netBarManageSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from netBarSys import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('mguser/', views.mguser, name='mguser'),
    path('logout/', views.logout, name='logout'),
    path('myinfo/', views.myinfo, name='myinfo'),
    path('onlineuser/', views.onlineuser, name='onlineuser'),
    path('adduser/', views.adduser, name='adduser'),
    path('deluser/<user_id>', views.deluser, name='deluser'),
    path('forceoffline/<user_id>', views.forceoffline, name='forceoffline'),
    path('modifypsw', views.modifypsw, name='modifypsw'),
]
