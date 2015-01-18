from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.forms import PickupForm
from accounts.models import Donor
from app.models import DonationCenter

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Pickup(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    #form = PickupForm(['pickup_name': Donor.objects.filter(user=request.user)[0].user.username])
    #print(form.fields['pickup_name'])
    #print(Donor.objects.filter(user=request.user)[0].user.username)

    form = PickupForm(initial={'pickup_name':Donor.objects.filter(user=request.user)[0].user.username, 'pickup_address':Donor.objects.filter(user=request.user)[0].address.__str__(), 'dropoff': DonationCenter.objects.filter(address__state='PA')})

    return render(request, 'pickup.html', {'form':form})

def Tracking(request):
    return render(request, 'tracking.html')
