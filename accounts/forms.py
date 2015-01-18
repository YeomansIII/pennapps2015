from django import forms
from accounts.models import Donor
from app.models import Address
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor

DonorUserFormSet = inlineformset_factory(User,Donor)
DonorAddressFormSet = inlineformset_factory(Address,Donor)
