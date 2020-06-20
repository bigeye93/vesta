from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item Definition """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CoverageDataType(AbstractItem):

    pass


class Testcoverage(core_models.TimeStampedModel):

    """ Testcoverage Model Definition """

    # project info
    product = 1
    capacities = 1
    nand_type = 1
    soc_type = 1
    phase = 1

    # testcase info
    testcase = 1  # foreing

    # issue info
    linked_issue = 1  # many to many

    # coverage data

    # def __str__(self):
    #     return f"{self.room} - {self.check_in}"
