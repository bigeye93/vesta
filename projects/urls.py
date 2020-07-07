from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("<int:pk>", views.project_detail, name="detail"),
    path("<int:pk>/some_view", views.some_view, name="some_view"),
]
