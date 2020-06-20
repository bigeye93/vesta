from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ProductType(AbstractItem):

    pass


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

    product = 1
    capacities = 1
    nand_type = 1
    soc_type = 1
    phase = 1

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_INPROGRESS
    )
    verification_start = models.DateField()
    verification_end = models.DateField()

    testcases = 1  # many to many

    progress = 1
    linked_issue = 1

    # guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # def __str__(self):
    #     return f"{self.room} - {self.check_in}"
