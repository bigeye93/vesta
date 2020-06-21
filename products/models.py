from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class ProductType(AbstractItem):

    pass


class CapacityType(AbstractItem):

    pass


class NandType(AbstractItem):

    pass


class SocType(AbstractItem):

    pass


class Product(core_models.TimeStampedModel):

    """ Product Model Definition """

    # product info
    product = models.ForeignKey(
        "ProductType", null=True, blank=True, on_delete=models.SET_NULL
    )
    capacities = models.ManyToManyField("CapacityType", blank=True)
    nand_types = models.ManyToManyField("NandType", blank=True)
    soc_types = models.ManyToManyField("SocType", blank=True)

    def __str__(self):
        return str(self.product)
