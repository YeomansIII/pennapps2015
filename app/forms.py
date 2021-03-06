from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Pickup
from accounts.models import Donor

class PickupForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = True
    helper.form_id = 'PickupForm'
    helper.form_action = 'pickup'
    helper.add_input(Submit('_qoute', 'Quote'))
    helper.add_input(Submit('_submit', 'Submit'))

    class Meta:
        model = Pickup
        fields = ("manifest", "pickup_name", "pickup_address", "pickup_phone_number", "pickup_business_name", "pickup_notes", "dropoff")

#class PickupForm(forms.Form):
	#class Meta:
   #     fields = ("name", "caption", "photos")
