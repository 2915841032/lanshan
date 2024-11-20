from django.urls import path
from . import views

urlpatterns = [
    path('captcha/', views.captcha, name='captcha'),
    path('verify_captcha/', views.verify_captcha, name='verify_captcha'),
    path('', views.index, name='index'),
]
