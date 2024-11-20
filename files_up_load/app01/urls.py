# urls.py

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'app01'
urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),  # 上传视图
    path('download/<int:file_id>/', views.download_file, name='download_file'),  # 下载视图
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 让开发环境支持文件访问
