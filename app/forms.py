from django import forms
 
class PickupForm(forms.ModelForm):
    class Meta:
        model = Pickup
