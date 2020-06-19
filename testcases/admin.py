from django.contrib import admin
from . import models


@admin.register(
    models.PlatformType, models.CustomerType, models.PhaseType, models.ConditionType
)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Testcase)
class TestcaseAdmin(admin.ModelAdmin):

    """ Testcase Admin Definition """

    pass
