from django.shortcuts import render
from app.forms import PickupForm
from accounts.models import Donor

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Pickup(request):
	form = PickupForm()
	form.fields['pickup_name'].queryset = Donor.objects.filter(user=request.user)
	return render(request, 'pickup.html', {'form':PickupForm})

def Tracking(request):
    return render(request, 'tracking.html')
