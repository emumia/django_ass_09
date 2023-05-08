from django.urls import path
from . import views

urlpatterns = [
    path("career", views.career, name="career"),
]