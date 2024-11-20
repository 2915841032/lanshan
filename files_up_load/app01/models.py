# models.py

from django.db import models


class UploadedFile(models.Model):
	file = models.FileField(upload_to='uploads/')  # 文件上传到 uploads/ 目录
	uploaded_at = models.DateTimeField(auto_now_add=True)  # 文件上传时间

	def __str__(self):
		return self.file.name
