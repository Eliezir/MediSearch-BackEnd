from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.get_medicines, name='medicines'),
    path('filter/', controllers.filter_medicines, name='filter_medicines'),
]