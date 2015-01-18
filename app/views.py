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

    form = PickupForm(initial={'pickup_name':Donor.objects.filter(user=request.user)[0].user.username,
    	'pickup_address':Donor.objects.filter(user=request.user)[0].address.__str__(),
    	'pickup_phone_number':Donor.objects.filter(user=request.user)[0].phone_number,
    	'pickup_business_name':Donor.objects.filter(user=request.user)[0].business_name,
    	'dropoff': DonationCenter.objects.filter(address__state='PA')})

    donation_centers = DonationCenter.objects.filter(address__city='Philladelphia')

    '''if request.method == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
        	post_data = [('manifest',request.POST.get("manifest", "")), ('pickup_name',request.POST.get("pickup_name", "")), 
        		('pickup_address',request.POST.get("pickup_address", "")), 	('pickup_phone_number',request.POST.get("pickup_phone_number", ""), 
        		('pickup_business_name',request.POST.get("pickup_business_name", "")), ('pickup_notes',request.POST.get("pickup_notes", "")), 
        		('dropoff_name',request.POST.get("dropoff_name", "")), ('dropoff_address',request.POST.get("dropoff_address", "")), 
        		('dropoff_phone_number',request.POST.get("dropoff_phone_number", "")), ('dropoff_business_name',request.POST.get("dropoff_business_name", "")), 
        		('dropoff_notes',request.POST.get("dropoff_notes", "")), ('quote_id',request.POST.get("quote_id", "")), ]     # a sequence of two element tuples
			result = urllib2.urlopen('https://api.postmates.com/v1/customers/cus_KAavEXNQhOREkF/deliveries', urllib.urlencode(post_data))
			content = result.read()
            return ''
    else:
        form = PickupForm()

    return render(request, 'pickup.html', {'form':form})

    if request.method == 'POST':
        form = PickupForm(request.POST)
        if form.is_valid():
        	post_data = [('pickup_address',request.POST.get("pickup_address", "")), ('dropoff_address',request.POST.get("dropoff_address", "")), ]     # a sequence of two element tuples
        	result = urllib2.urlopen('https://api.postmates.com/v1/customers/cus_KAavEXNQhOREkF/delivery_quotes', urllib.urlencode(post_data))
        	content = result.read()
        return content.fee
    else:
        form = PickupForm()

    return render(request, 'pickup.html', {'form':form})'''

    return render(request, 'pickup.html', {'form':form, 'donation_centers':donation_centers})

def Tracking(request):
    return render(request, 'tracking.html')
