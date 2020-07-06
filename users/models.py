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

    avatar = models.ImageField(upload_to="avatars", blank=True)
    empoyee_number = models.IntegerField(null=True, blank=True)
    coe = models.CharField(choices=COE_CHOICES, max_length=10, blank=True)
    part = models.CharField(choices=PART_CHOICES, max_length=10, blank=True)

    def get_full_name(self):
        full_name = super().last_name + super().first_name
        return full_name

    get_full_name.short_description = "Full name (kr)"

    def __str__(self):
        return self.get_full_name()
