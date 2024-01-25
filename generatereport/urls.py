from django.urls import path
from . import views
from .views import generate_csv


urlpatterns = [
    path('', views.index, name='index'),
    path('generate-csv/', generate_csv, name='generate_csv'),

]