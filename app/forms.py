from django import forms
from crispy_forms.helper import FormHelper
 
class UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
 
    class Meta:
        model = Pickup # Your user model