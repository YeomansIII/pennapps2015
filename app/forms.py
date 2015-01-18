from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Pickup
from accounts.models import Donor

class PickupForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_id = 'PickupForm'
    helper.form_action = 'submit_survey'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Pickup
        fields = ("manifest", "pickup_name", "dropoff_name")

#class PickupForm(forms.Form):
	#class Meta:
   #     fields = ("name", "caption", "photos")
