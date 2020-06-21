from django.contrib import admin
from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    """ Project Admin Definition """

    fieldsets = (
        ("Project Info", {"fields": ("product", "phase",)},),
        (
            "Verification Info",
            {
                "classes": ("collapse",),
                "fields": (
                    "status",
                    "verification_start",
                    "verification_end",
                    # "testcases",
                ),
            },
        ),
    )

    list_display = (
        "__str__",
        "product",
        "phase",
        "status",
        "verification_start",
        "verification_end",
    )

    list_filter = (
        "product",
        "status",
    )

    search_fields = ("product",)

    # filter_horizontal = ("testcases",)
