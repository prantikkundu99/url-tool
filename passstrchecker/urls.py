from django.urls import path
from .views import (
    passstrchecker,
)

urlpatterns = [

    path("", passstrchecker, name="passstrchecker"),
    

]