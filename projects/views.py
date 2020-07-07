import csv
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from .tables import ResultTable, ResultFilter
from . import models


def project_detail(request, pk):
    project = models.Project.objects.get(pk=pk)
    filter = ResultFilter(request.GET, queryset=project.testresults.all())
    testresults = ResultTable(filter.qs)
    testresults.paginate(page=request.GET.get("page", 1), per_page=25)
    RequestConfig(request, paginate={"per_page": 25}).configure(testresults)

    return render(
        request,
        "projects/detail.html",
        {"project": project, "testresults": testresults, "filter": filter},
    )


def some_view(request, pk):

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="somefilename.csv"'

    project = models.Project.objects.get(pk=pk)
    filter = ResultFilter(request.GET, queryset=project.testresults.all())
    testresults = ResultTable(filter.qs)

    export_data = testresults.rows.data.data

    writer = csv.writer(response)

    for data in export_data:
        writer.writerow(
            [
                data,
                data.testcase.category,
                data.testcase.sub_category,
                data.testcase.owner.email,
            ]
        )

    return response
