from django.contrib import admin
from .models import Profile, Role

admin.site.site_title = "Scholarship Portal"
admin.site.site_header = "Scholarship Portal"

admin.site.register(Profile)
admin.site.register(Role)