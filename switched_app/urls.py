from django.urls import path
from . import views

urlpatterns = [

    # Map index url to home page
    path('', views.index, name='index'),
]