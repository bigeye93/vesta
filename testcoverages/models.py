from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CoverageKeyType(AbstractItem):

    group_name = models.CharField(max_length=200)
    key_name = models.CharField(max_length=200)
    data_type = models.CharField(max_length=200)


class Testcoverage(core_models.TimeStampedModel):

    """ Testcoverage Model Definition """

    STATUS_NORMAL = "Normal"
    STATUS_ABNORMAL = "Abnormal"
    STATUS_WARNING = "Warning"

    STATUS_CHOICES = (
        (STATUS_NORMAL, "Normal"),
        (STATUS_ABNORMAL, "Abnormal"),
        (STATUS_WARNING, "Warning"),
    )

    # coverage key info
    key_id = models.ForeignKey(
        "CoverageKeyType", null=True, blank=True, on_delete=models.SET_NULL
    )

    # project info
    project = models.ForeignKey(
        "projects.Project", null=True, blank=True, on_delete=models.SET_NULL
    )

    # testcase info
    testcase = models.ForeignKey(
        "testcases.Testcase", null=True, blank=True, on_delete=models.SET_NULL
    )

    # coverage data
    value = models.IntegerField(null=True, blank=True)
    value_diff = models.IntegerField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_NORMAL
    )

    def __str__(self):
        if self.project is None or self.testcase is None:
            return "[temp] update project & testcase info"
        else:
            return f"{str(self.updated)} - pid{str(self.project.product_id)}_{str(self.project.fw_rev)}_{str(self.testcase.name)}_{str(self.key_id)}"
