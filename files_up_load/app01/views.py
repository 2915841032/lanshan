# views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile
from django.core.exceptions import ValidationError

# views.py

from django.http import FileResponse, Http404


def upload_file(request):
	if request.method == 'POST' and request.FILES.getlist('files'):
		files = request.FILES.getlist('files')  # 获取多个文件
		for file in files:
			try:
				# 保存文件到数据库模型中
				uploaded_file = UploadedFile(file=file)
				uploaded_file.save()
			except ValidationError as e:
				return HttpResponse(f"Error: {e}")

		return HttpResponse("Files uploaded successfully")

	return render(request, 'upload.html')


def download_file(request, file_id):
	try:
		file = UploadedFile.objects.get(id=file_id)
		return FileResponse(open(file.file.path, 'rb'), as_attachment=True, filename=file.file.name)
	except UploadedFile.DoesNotExist:
		raise Http404("File not found")


# views.py

import os
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


def upload_chunked(request):
	if request.method == 'POST':
		file = request.FILES.get('file')
		chunk = int(request.POST.get('chunk'))
		total_chunks = int(request.POST.get('total_chunks'))

		# Create a temporary file to store the chunk
		temp_file_path = os.path.join(settings.MEDIA_ROOT, f'temp_{file.name}')
		with open(temp_file_path, 'ab') as temp_file:
			temp_file.write(file.read())

		# If all chunks are uploaded, process the file
		if chunk == total_chunks - 1:
			# Do something with the full file (e.g., move to final location)
			pass

		return JsonResponse({"message": "Chunk uploaded successfully"})
