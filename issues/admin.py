from django.contrib import admin
from . import models


@admin.register(models.Issue)
class IssueAdmin(admin.ModelAdmin):

    """ Issue Admin Definition """

    pass
