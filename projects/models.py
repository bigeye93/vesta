from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class Project(core_models.TimeStampedModel):

    """ Project Model Definition """

    STATUS_INPROGRESS = "In progress"
    STATUS_DONE = "Done"
    STATUS_CANCELED = "Canceled"

    STATUS_CHOICES = (
        (STATUS_INPROGRESS, "In progress"),
        (STATUS_DONE, "Done"),
        (STATUS_CANCELED, "Canceled"),
    )

    # project info
    product = models.ForeignKey(
        "products.Product",
        related_name="projects",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    phase = models.CharField(max_length=20)
    fw_rev = models.CharField(max_length=20)
    customer = models.ForeignKey(
        "products.CustomerType", null=True, blank=True, on_delete=models.SET_NULL
    )

    # verification info
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_INPROGRESS
    )
    verification_start = models.DateField(null=True, blank=True)
    verification_end = models.DateField(null=True, blank=True)

    def __str__(self):
        if self.product is None or self.customer is None:
            return "[temp] update product & customer info"
        else:
            return f"{str(self.product)}_{self.phase}_{self.customer}_{self.fw_rev}"
