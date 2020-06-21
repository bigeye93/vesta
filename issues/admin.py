from django.contrib import admin
from . import models


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):

    """ Issue Admin Definition """

    fieldsets = (
        ("Project Info", {"fields": ("project",)},),
        ("Testcase Info", {"fields": ("testcases",)},),
        (
            "Jira Info",
            {"fields": ("jira_number", "jira_status", "date_opened", "assignee",),},
        ),
    )
