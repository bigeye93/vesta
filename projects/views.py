from django.urls import reverse
from django.shortcuts import render, redirect
from .tables import ResultTable, ResultFilter
from . import models


def project_detail(request, pk):
    project = models.Project.objects.get(pk=pk)
    filter = ResultFilter(request.GET, queryset=project.testresults.all())
    testresults = ResultTable(filter.qs)
    testresults.paginate(page=request.GET.get("page", 1), per_page=25)
    return render(
        request,
        "projects/detail.html",
        {"project": project, "testresults": testresults, "filter": filter},
    )
