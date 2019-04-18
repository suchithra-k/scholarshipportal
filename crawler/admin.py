from django.contrib import admin

from .models import Scholarship, SchedulerAudit, ScholarshipEligibility

class ScholarshipEligibilityInline(admin.StackedInline):
    model = ScholarshipEligibility

class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('title', 'url','expiry_date')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}

    inlines = [
        ScholarshipEligibilityInline,
    ]

class SchedulerAuditAdmin(admin.ModelAdmin):
    list_display = ('task', 'last_runtime','status','remarks')
    search_fields = ['task']

admin.site.register(Scholarship, ScholarshipAdmin)
admin.site.register(SchedulerAudit, SchedulerAuditAdmin)
