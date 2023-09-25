from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ProgrammerDetailView.as_view(), name="details"),
    path("programmer", views.add_programmer, name="add_programmer"),
   
]