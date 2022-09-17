from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("",views.my_soap_application,name="soap_sum"),
]
