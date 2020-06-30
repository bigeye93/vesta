from django.db import models
from core import models as core_models


class Issue(core_models.TimeStampedModel):

    """ Issue Model Definition """

    # project info
    project = models.ForeignKey(
        "projects.Project",
        related_name="issues",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # testcase info
    testcase = models.ForeignKey(
        "testcases.Testcase",
        related_name="issues",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    # jira info
    jira_number = models.CharField(max_length=10)
    # jira_status = models.CharField(max_length=10)
    # date_opened = models.DateField(null=True, blank=True)
    # assignee = models.ForeignKey(
    #     "users.User", null=True, blank=True, on_delete=models.SET_NULL
    # )

    def __str__(self):
        return str(self.jira_number)
