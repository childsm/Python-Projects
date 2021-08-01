from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
#line 18 says in the this directory (. means this dir) use the file views

urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),

]
