from django.contrib import admin
from . import models


@admin.register(
    models.ProductType, models.CapacityType, models.NandType, models.SocType
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):

    """ Product Admin Definition """

    def get_related_testcases(self, obj):
        related_issues = obj.testcases.count()
        return related_issues

    get_related_testcases.short_description = "testcases"

    list_display = ("product", "get_related_testcases")

    list_filter = (
        "nand_types",
        "soc_types",
    )

    filter_horizontal = (
        "capacities",
        "nand_types",
        "soc_types",
    )
