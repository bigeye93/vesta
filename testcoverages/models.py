from django.db import models
from core import models as core_models


# class AbstractItem(core_models.TimeStampedModel):

#     """ Abstract Item Definition """

#     name = models.CharField(max_length=80)

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.name


# class CoverageDataType(AbstractItem):

#     pass


class Testcoverage(core_models.TimeStampedModel):

    """ Testcoverage Model Definition """

    # project info
    project = models.ForeignKey(
        "projects.Project", null=True, blank=True, on_delete=models.SET_NULL
    )

    # testcase info
    testcase = models.ForeignKey(
        "testcases.Testcase", null=True, blank=True, on_delete=models.SET_NULL
    )

    # coverage data

    # def __str__(self):
    #     return self.jira_number
