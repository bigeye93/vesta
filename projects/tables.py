import django_tables2 as tables
import django_filters
from django.db import models as db_models
from testresults import models as testresult_models


class ResultTable(tables.Table):
    class Meta:
        model = testresult_models.Testresult
        row_attrs = {"data-id": lambda record: record.pk}

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


class ResultFilter(django_filters.FilterSet):
    class Meta:
        model = testresult_models.Testresult
        fields = [
            "testcase__category",
            "testcase__sub_category",
            "testcase__owner",
        ]

        filter_overrides = {
            db_models.CharField: {
                "filter_class": django_filters.CharFilter,
                "extra": lambda f: {"lookup_expr": "icontains",},
            }
        }

        fields_labels = {
            "testcase__category": "Category",
            "testcase__sub_category": "Sub Sategory",
            "testcase__owner": "Owner",
        }

    def __init__(self, *args, **kwargs):
        super(ResultFilter, self).__init__(*args, **kwargs)
        self.filters["testcase__category"].label = "Category"
        self.filters["testcase__sub_category"].label = "Sub Category"
        self.filters["testcase__owner"].label = "Owner"
