from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.name)


class CapacityType(AbstractItem):

    pass


class NandType(AbstractItem):

    pass


class SocType(AbstractItem):

    pass


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
        "products.Product", null=True, blank=True, on_delete=models.SET_NULL
    )
    phase = models.IntegerField(null=True, blank=True)

    # verification info
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_INPROGRESS
    )
    verification_start = models.DateField(null=True, blank=True)
    verification_end = models.DateField(null=True, blank=True)

    # TODO
    # testcases = models.ManyToManyField("testcases.Testcase", blank=True)

    # TODO
    # linked_issues = models.ManyToManyField("issues.Issue", blank=True)

    def __str__(self):
        return f"{str(self.product)} - phase{self.phase}"
