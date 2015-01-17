from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Pickup(request):
    return render(request, 'index.html')

def Tracking(request):
    return render(request, 'index.html')
