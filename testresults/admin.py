from django.contrib import admin
from . import models


@admin.register(models.Testresult)
class TestresultAdmin(admin.ModelAdmin):

    """ Testresult Admin Definition """

    list_display = (
        "__str__",
        "project",
        "testcase",
        "status",
        "description",
    )

    list_filter = (
        "project",
        "testcase",
    )

    search_fields = (
        "project",
        "testcase",
    )
