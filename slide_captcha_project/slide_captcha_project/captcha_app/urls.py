from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_captcha/', views.get_captcha, name='get_captcha'),
    path('verify_captcha/', views.verify_captcha, name='verify_captcha'),
]