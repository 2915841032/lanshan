from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
	# return render(request,'app01/index.html')
	return HttpResponse('app01 index')




def my_view(request):
	return JsonResponse({"message": "You are authorized!"})
