from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Pickup

class PickupForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Pickup
