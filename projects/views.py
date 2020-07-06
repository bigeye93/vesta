from django.urls import reverse
from django.shortcuts import render, redirect
from .tables import ResultTable, ResultFilter
from . import models


def project_detail(request, pk):
    project = models.Project.objects.get(pk=pk)
    testresults = ResultTable(project.testresults.all())
    testresults.paginate(page=request.GET.get("page", 1), per_page=25)
    filter = ResultFilter(request.GET, project.testresults.all())
    return render(
        request,
        "projects/detail.html",
        {"project": project, "testresults": testresults, "filter": filter},
    )

