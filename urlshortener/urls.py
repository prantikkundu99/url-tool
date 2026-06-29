from django.urls import path
from .views import (
    urlshort,
    urlredirect,
)

urlpatterns = [

    path("", urlshort, name="urlshort"),
    path("<str:token>/", urlredirect, name="urlresolver"),

]