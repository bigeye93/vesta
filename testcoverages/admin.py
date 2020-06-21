from django.contrib import admin
from . import models


# @admin.register(models.CoverageDataType)
# class ItemAdmin(admin.ModelAdmin):

#     """ Item Admin Definition """

#     pass


@admin.register(models.Testcoverage)
class TestcoverageAdmin(admin.ModelAdmin):

    """ Testcoverage Admin Definition """

    pass
