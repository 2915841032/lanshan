# fileupload/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include('app01.urls',"upload")),  # 引入上传文件的路由
]

# 配置媒体文件的路由
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
