from . import views
from django.urls import path, include

app_name = "preparation"

urlpatterns = [
    path("data/", views.TodoView.as_view(), name="data"),
    path("detail/<int:id>/", views.DetailView.as_view(), name="detail"),
]
