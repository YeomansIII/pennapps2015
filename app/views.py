from django.shortcuts import render
from app.forms import PickupForm

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Pickup(request):
    return render(request, 'pickup.html', {'form':PickupForm})

def Tracking(request):
    return render(request, 'tracking.html')
