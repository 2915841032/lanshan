from django.urls import path
from .views import protected_view

urlpatterns = [
    path("protected/", protected_view),
]