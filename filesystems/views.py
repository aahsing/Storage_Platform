from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'filesystems/index.html')

def createdir(request):
    return render(request, 'filesystems/createdir.html')

def quota(request):
    return render(request, 'filesystems/quota.html')