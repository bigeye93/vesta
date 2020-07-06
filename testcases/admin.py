from django.contrib import admin
from . import models


@admin.register(
    models.CustomerType, models.PhaseType, models.ConditionType, models.LbaFormatType
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
                    "id_ext",
                    "platform",
                    "name",
                    "script",
                    "args",
                    "category",
                    "sub_category",
                    "owner",
                    "description",
                )
            },
        ),
        (
            "Filtering Info",
            {
                # "classes": ("collapse",),
                "fields": (
                    "condition",
                    "phases",
                    "customers",
                    "lba_formats",
                    "products",
                ),
            },
        ),
    )

    list_display = (
        "id_ext",
        "platform",
        "name",
        "category",
        "sub_category",
        "owner",
        "get_related_issues",
    )

    list_filter = (
        "platform",
        "products",
        "category",
        "sub_category",
    )

    search_fields = (
        "^id_ext",
        "products",
        "category",
        "sub_category",
        "name",
    )

    filter_horizontal = (
        "phases",
        "customers",
        "lba_formats",
        "products",
    )
