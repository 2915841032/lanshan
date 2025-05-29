"""voting_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
# urls.py

urlpatterns = [
    # 首页视图，显示所有学科信息
    path('', show_subjects),
    # 学科老师视图，显示指定学科的老师信息
    path('teachers/', show_teachers),
    # 后台管理URL
    path('admin/', admin.site.urls),
]
