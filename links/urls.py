from django.urls import path

from links.views import home

urlpatterns = [
    path('', home)
]
