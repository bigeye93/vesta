import django_tables2 as tables
from django_filters import FilterSet
from testresults import models as testresult_models

# from testresults import Testresult


class ResultTable(tables.Table):
    class Meta:
        model = testresult_models.Testresult
        row_attrs = {"data-id": lambda record: record.pk}
        template_name = "django_tables2/bootstrap.html"

        fields = (
            "testcase",
            "testcase.category",
            "testcase.sub_category",
            "testcase.name",
            "testcase.owner",
            "status",
            "description",
            "updated",
        )


class ResultFilter(FilterSet):
    class Meta:
        model = testresult_models.Testresult
        fields = [
            "testcase__category",
            "testcase__sub_category",
            "testcase__owner",
        ]

