from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Pickup

class PickupForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_id = 'PickupForm'
    helper.form_action = 'submit_survey'
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Pickup
