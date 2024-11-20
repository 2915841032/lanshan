# upload/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.conf import settings
from .forms import FileUploadForm
from .models import UploadedFile
import os


# 文件上传视图
def upload_file(request):
	if request.method == 'POST' and request.FILES['file']:
		form = FileUploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()  # 保存文件
			return redirect('upload:success')
	else:
		form = FileUploadForm()

	return render(request, 'upload/upload_file.html', {'form': form})

# 文件下载视图
def download_file(request, file_id):
	try:
		file_record = UploadedFile.objects.get(id=file_id)
		file_path = file_record.file.path
		if os.path.exists(file_path):
			response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
			response['Content-Disposition'] = f'attachment; filename={file_record.file.name}'
			return response
		else:
			return HttpResponse('File not found', status=404)
	except UploadedFile.DoesNotExist:
		return HttpResponse('File not found', status=404)


# 上传成功页面
def success(request):
	return HttpResponse('File uploaded successfully!')

