from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
        dic = {'name':'post','age':18}
        return render(request, 'index.html',locals())
    if request.method == 'GET':
        print(request.GET)
        dic = {'name':'get','age':18}
        return render(request, 'index.html',locals())