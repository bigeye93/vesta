from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom User Model """

    COE_ESSD = "eSSD PV"
    COE_CSSD = "cSSD PV"

    COE_CHOICES = (
        (COE_ESSD, "eSSD PV"),
        (COE_CSSD, "cSSD PV"),
    )

    PART_FTL = "FTL"
    PART_HIL = "HIL"
    PART_PVT = "PVT"
    PART_MANAGER = "Manager"
    PART_OTHER = "Other"

    PART_CHOICES = (
        (PART_FTL, "FTL"),
        (PART_HIL, "HIL"),
        (PART_PVT, "PVT"),
        (PART_MANAGER, "Manager"),
        (PART_OTHER, "Other"),
    )

    avatar = models.ImageField(blank=True)
    empoyee_number = models.IntegerField(null=True, blank=True)
    coe = models.CharField(choices=COE_CHOICES, max_length=10, blank=True)
    part = models.CharField(choices=PART_CHOICES, max_length=10, blank=True)
    superuser = models.BooleanField(default=False)
    # project # many to many
