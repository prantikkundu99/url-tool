from django.urls import path
from .views import (
   passgenerator 
)

urlpatterns = [

    path("", passgenerator, name="passgenerator"),

]