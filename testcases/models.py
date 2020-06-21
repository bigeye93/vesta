from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


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

    # basic info
    uid = models.CharField(max_length=20)
    platorm = models.ForeignKey(
        "PlatformType", null=True, blank=True, on_delete=models.SET_NULL
    )
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(
        "users.User", null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField(blank=True)

    # filtering info
    products = models.ManyToManyField(
        "products.Product", related_name="testcases", blank=True
    )
    customers = models.ManyToManyField("CustomerType", blank=True)
    phases = models.ManyToManyField("PhaseType", blank=True)
    condition = models.ForeignKey(
        "ConditionType", null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return str(self.uid)
