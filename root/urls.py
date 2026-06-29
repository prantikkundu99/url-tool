from django.urls import path, include

urlpatterns = [

    path("passgen/", include("passgenerator.urls")),
    path("passstrchecker/", include("passstrchecker.urls")),
    path("", include("urlshortener.urls"))
]
