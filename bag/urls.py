"""zspices Bag App URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
