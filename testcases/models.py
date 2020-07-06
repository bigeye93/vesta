from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class CustomerType(AbstractItem):
    # class Meta:
    #     verbose_name_plural = "Platform Types"

    # class Meta:
    #     verbose_name = "Platform Types"
    #     ordering = ["name"]
    pass


class PhaseType(AbstractItem):

    pass


class ConditionType(AbstractItem):

    pass


class LbaFormatType(AbstractItem):

    pass


class Testcase(core_models.TimeStampedModel):

    """ Testcase Model Definition """

    # basic info
    id_ext = models.CharField(max_length=20)
    platform = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    script = models.CharField(max_length=200)
    args = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    sub_category = models.CharField(max_length=200)
    owner = models.ForeignKey(
        "users.User", null=True, blank=True, on_delete=models.SET_NULL
    )
    description = models.TextField(blank=True)

    # filtering info
    condition = models.ForeignKey(
        "ConditionType", null=True, blank=True, on_delete=models.SET_NULL
    )
    phases = models.ManyToManyField("PhaseType", blank=True)
    customers = models.ManyToManyField("CustomerType", blank=True)
    lba_formats = models.ManyToManyField("LbaFormatType", blank=True)
    products = models.ManyToManyField(
        "products.Product", related_name="testcases", blank=True
    )

    def __str__(self):
        return str(self.id_ext)
