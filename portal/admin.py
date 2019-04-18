from django.contrib import admin
from users.models import Organisation


class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ['name']

admin.site.register(Organisation, OrganisationAdmin)
