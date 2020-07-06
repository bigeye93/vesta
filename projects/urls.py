from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("<int:pk>", views.project_detail, name="detail"),
]
