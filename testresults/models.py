from django.db import models
from core import models as core_models


class Testresult(core_models.TimeStampedModel):

    """ Testresult Model Definition """

    STATUS_INPROGRESS = "In progress"
    STATUS_PASSED = "Passed"
    STATUS_FAILED = "Failed"
    STATUS_PENDING = "Pending"
    STATUS_NA = "N/A"

    STATUS_CHOICES = (
        (STATUS_INPROGRESS, "In progress"),
        (STATUS_PASSED, "Passed"),
        (STATUS_FAILED, "Failed"),
        (STATUS_PENDING, "Pending"),
        (STATUS_NA, "N/A"),
    )

    testcase = models.ForeignKey(
        "testcases.Testcase",
        related_name="testresults",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    project = models.ForeignKey(
        "projects.Project",
        related_name="testresults",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_INPROGRESS
    )

    description = models.TextField(blank=True)

    def __str__(self):
        if self.project is None or self.testcase is None:
            return "[temp] update project & testcase info"
        else:
            return f"{str(self.updated)} - pid{str(self.project.product_id)}_{str(self.project.fw_rev)}_{str(self.testcase.name)}"
