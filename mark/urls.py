from django.urls import path
from . import views

urlpatterns = [
    path('', views.showPhoto, name='showPhoto')
]