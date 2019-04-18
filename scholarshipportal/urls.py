"""
scholarshipportal URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('crawler/', include('crawler.urls')),
    path('portal/', include('portal.urls')),
]
