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

    list_display = ("product",)

    list_filter = (
        "nand_types",
        "soc_types",
    )

    filter_horizontal = (
        "capacities",
        "nand_types",
        "soc_types",
    )
