# upload/urls.py
from django.urls import path
from . import views
app_name = 'app01'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('success/', views.success, name='success'),
]