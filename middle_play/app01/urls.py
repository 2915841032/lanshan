
from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index),
    path('my-view/', my_view),
]
