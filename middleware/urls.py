
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("/withthreads",views.middwarefun,name="middwarefun"),
    path("/withoutthreads",views.middlewarewithoutthreads,name="middlewarewithoutthreads"),
]
