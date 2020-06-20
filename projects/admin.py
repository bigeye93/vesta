from django.contrib import admin
from . import models


@admin.register(
    models.ProductType, models.CapacityType, models.NandType, models.SocType
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    """ Project Admin Definition """

    pass
