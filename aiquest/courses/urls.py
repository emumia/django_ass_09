from django.urls import path
from . import views

urlpatterns = [
    path("crs", views.course, name="courses"),
    path("dj", views.django, name="django_web_development"),
    path("ml", views.machine_learning, name="machine Learning"),
    path("dl", views.deep_learning, name="deep Learning"),   
    path("data_analysis", views.data_analysis, name="data_analysis"),
    path("cloud-computing", views.cloud_computing, name="cdc"),
    path("python", views.python, name="python"),
    path("Big_data", views.big_data, name="big_data"),
    path("st", views.statistics, name="stat"),
    path("sql", views.sql, name="sql"),
]
