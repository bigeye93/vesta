from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    """ Project Admin Definition """

    def get_related_issues(self, obj):
        related_issues = obj.issues.count()
        return related_issues

    get_related_issues.short_description = "issues"

    fieldsets = (
        ("Project Info", {"fields": ("product", "phase", "fw_rev", "customer")},),
        (
            "Verification Info",
            {
                "classes": ("collapse",),
                "fields": ("status", "verification_start", "verification_end",),
            },
        ),
    )

    list_display = (
        "__str__",
        "product",
        "phase",
        "fw_rev",
        "get_related_issues",
    )

    list_filter = ("product",)

    search_fields = ("product",)
