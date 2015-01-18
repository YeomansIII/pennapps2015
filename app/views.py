from django.shortcuts import render
from django.http import HttpResponseRedirect
from app.forms import PickupForm
from accounts.models import Donor
from app.models import DonationCenter, Pickup
import requests
import json

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Privacy(request):
    return render(request, 'privacy.html')

def PickupPage(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/')
    #form = PickupForm(['pickup_name': Donor.objects.filter(user=request.user)[0].user.username])
    #print(form.fields['pickup_name'])
    #print(Donor.objects.filter(user=request.user)[0].user.username)

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

    return render(request, 'pickup.html', {'form':form})'''
    qoute_val=None
    if request.method == 'POST':
        if '_qoute' in request.POST:

            form = PickupForm(request.POST)
            if form.is_valid():
                ##Qoute request
                s = requests.Session()
                s.auth = ('c79fe220-4ac4-4771-b2cc-7230fcfbcca9', '')
                post_data = {'pickup_address':form.cleaned_data['pickup_address'], 'dropoff_address':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].address.__str__()}     # a sequence of two element tuples
                response = s.post('https://api.postmates.com/v1/customers/cus_KAavEXNQhOREkF/delivery_quotes', data=post_data)
                content = response.content
                jay = json.loads(content)
                qoute_val = str(jay['fee'])
                cents = qoute_val[2:]
                qoute_val = qoute_val[:2]+"."+cents
                #print(content)
            #return content.fee
        if '_submit' in request.POST:

            form = PickupForm(request.POST)
            if form.is_valid():

                ##Make new qoute request to send with delivery request
                s = requests.Session()
                s.auth = ('c79fe220-4ac4-4771-b2cc-7230fcfbcca9', '')
                post_data = {'pickup_address':form.cleaned_data['pickup_address'], 'dropoff_address':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].address.__str__()}     # a sequence of two element tuples
                response = s.post('https://api.postmates.com/v1/customers/cus_KAavEXNQhOREkF/delivery_quotes', data=post_data)
                content = response.content
                jay = json.loads(content)
                qoute_val = str(jay['fee'])
                cents = qoute_val[2:]
                qoute_val = qoute_val[:2]+"."+cents
                qoute_id = jay['id']

                ##Delivery Request
                s = requests.Session()
                s.auth = ('c79fe220-4ac4-4771-b2cc-7230fcfbcca9', '')
                post_data = {'manifest':form.cleaned_data['manifest'], 'pickup_name':form.cleaned_data['pickup_name'],
                    'pickup_address':form.cleaned_data['pickup_address'], 'pickup_phone_number':form.cleaned_data['pickup_phone_number'],
                    'pickup_business_name':form.cleaned_data['pickup_business_name'], 'pickup_notes':form.cleaned_data['pickup_notes'],
                    'dropoff_name':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].name, 'dropoff_address':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].address.__str__(),
                    'dropoff_phone_number':form.cleaned_data['pickup_phone_number'], 'dropoff_business_name':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].name,
                    'dropoff_notes':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].dropoff_notes, 'quote_id':qoute_id }     # a sequence of two element tuples
                response = s.post('https://api.postmates.com/v1/customers/cus_KAavEXNQhOREkF/deliveries', data=post_data)
                content = response.content
                jay = json.loads(content)
                deliveryid = jay['id']
                qoute_val = content


                pickup_obj = Pickup.objects.create(manifest=form.cleaned_data['manifest'], pickup_name=form.cleaned_data['pickup_name'], pickup_address=form.cleaned_data['pickup_address'], pickup_phone_number=form.cleaned_data['pickup_phone_number'], pickup_business_name=form.cleaned_data['pickup_business_name'], pickup_notes=form.cleaned_data['pickup_notes'], dropoff=DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0], delivery_id=deliveryid, quote_id=qoute_id)
                pickup_obj.save()
                donor = Donor.objects.filter(user=request.user)[0]
                donor.history.add(pickup_obj)
                donor.save()
                return HttpResponseRedirect('/tracking/')

    else:
        form = PickupForm(initial={'pickup_name':Donor.objects.filter(user=request.user)[0].user.username,
            'pickup_address':Donor.objects.filter(user=request.user)[0].address.__str__(),
            'pickup_phone_number':Donor.objects.filter(user=request.user)[0].phone_number,
            'pickup_business_name':Donor.objects.filter(user=request.user)[0].business_name,
            'dropoff': DonationCenter.objects.filter(address__state='PA')})

    #return render(request, 'pickup.html', {'form':form})

    return render(request, 'pickup.html', {'form':form, 'donation_centers':donation_centers, 'qoute':qoute_val})

def Tracking(request):

    s = requests.Session()
    s.auth = ('c79fe220-4ac4-4771-b2cc-7230fcfbcca9', '')
    post_data = {'pickup_address':form.cleaned_data['pickup_address'], 'dropoff_address':DonationCenter.objects.filter(name=form.cleaned_data['dropoff'])[0].address.__str__()}     # a sequence of two element tuples
    response = s.post('https://api.postmates.com/v1/customers/cus_KAavEXNQhOREkF/delivery_quotes', data=post_data)
    content = response.content
    jay = json.loads(content)


    return render(request, 'tracking.html')

def Profile(request):
    username = "Username: "+Donor.objects.filter(user=request.user)[0].user.username
    address = "Address: "+Donor.objects.filter(user=request.user)[0].address.__str__()
    phone_number = "Phone Number: "+Donor.objects.filter(user=request.user)[0].phone_number
    business_name = "Business Name: "+Donor.objects.filter(user=request.user)[0].business_name
    return render(request, 'profile.html', {'username':username, 'address':address, 'phone_number':phone_number, 'business_name':business_name})
