from django.contrib import admin
from . import models


@admin.register(
    models.PlatformType, models.CustomerType, models.PhaseType, models.ConditionType,
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Testcase)
class TestcaseAdmin(admin.ModelAdmin):

    """ Testcase Admin Definition """

    def get_related_issues(self, obj):
        related_issues = obj.issues.count()
        return related_issues

    get_related_issues.short_description = "issues"

    fieldsets = (
        (
            "Basic Info",
            {
                "fields": (
                    "uid",
                    "platorm",
                    "category",
                    "sub_category",
                    "name",
                    "owner",
                    "description",
                )
            },
        ),
        (
            "Filtering Info",
            {
                # "classes": ("collapse",),
                "fields": ("products", "customers", "phases", "condition",),
            },
        ),
    )

    list_display = (
        "uid",
        "category",
        "sub_category",
        "name",
        "owner",
        "get_related_issues",
    )

    list_filter = (
        "products",
        "category",
        "sub_category",
    )

    search_fields = (
        "^uid",
        "products",
        "category",
        "sub_category",
        "name",
    )

    filter_horizontal = (
        "products",
        "customers",
        "phases",
    )
