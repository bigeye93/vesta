from django.db import models
from core import models as core_models


class Issue(core_models.TimeStampedModel):

    """ Issue Model Definition """

    # product phase capacity
    product = 1  # foreign
    phase = 1  # foreign
    capacity = 1  # many to many

    jira_number = models.CharField(max_length=10)
    jira_status = 1  # Get from jira
    date_opened = 1  # Get from jira or date field
    assignee = models.ForeignKey("users.User", on_delete=models.PROTECT)
    testcase = models.ForeignKey("testcases.Testcase", on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product} - {self.jira_number}"
