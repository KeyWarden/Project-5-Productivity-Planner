"""pro_plan URL Configuration"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('profiles.urls')),
    path('', include('tasks.urls')),
]
