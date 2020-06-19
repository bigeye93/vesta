from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PlatformType(AbstractItem):
    # class Meta:
    #     verbose_name_plural = "Platform Types"

    # class Meta:
    #     verbose_name = "Platform Types"
    #     ordering = ["name"]

    pass


class CustomerType(AbstractItem):

    pass


class PhaseType(AbstractItem):

    pass


class ConditionType(AbstractItem):

    pass


class Testcase(core_models.TimeStampedModel):

    """ Testcase Model Definition """

    uid = models.CharField(max_length=20)
    name = models.CharField(max_length=140)
    platorm = models.ManyToManyField("PlatformType", blank=True)
    category = models.CharField(max_length=140)
    sub_category = models.CharField(max_length=140)
    owner = models.ForeignKey("users.User", on_delete=models.PROTECT)
    description = models.TextField()

    # project = models.ManyToManyField(RoomType, blank=True) # many to many
    customer = models.ManyToManyField("CustomerType", blank=True)
    phase = models.ManyToManyField("PhaseType", blank=True)
    condition = models.ManyToManyField("ConditionType", blank=True)

    # history = 1 # TBD
    # linked_issue = 1 # TBD

    def __str__(self):
        return self.name
