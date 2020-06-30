from django.contrib import admin
from . import models


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):

    """ Issue Admin Definition """

    fieldsets = (
        ("Project Info", {"fields": ("project",)},),
        ("Testcase Info", {"fields": ("testcase",)},),
        ("Jira Info", {"fields": ("jira_number",),},),
    )
