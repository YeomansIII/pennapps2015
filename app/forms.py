from django import forms
from crispy_forms.helper import FormHelper
from app.models import Pickup

class PickupForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False

    class Meta:
        model = Pickup
