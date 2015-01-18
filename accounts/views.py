from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import DonorUserFormSet, DonorAddressFormSet, DonorForm
from accounts.models import Donor
# Create your views here.

class DonorCreateView(CreateView):
    template_name = 'register.html'
    model = Donor
    form_class = DonorForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        donoruser_form = DonorUserFormSet()
        donoraddress_form = DonorAddressFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  donoruser_form=donoruser_form,
                                  donoraddress_form=donoraddress_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        donoruser_form = DonorUserFormSet(self.request.POST)
        donoraddress_form = DonorAddressFormSet(self.request.POST)
        if (form.is_valid() and donoruser_form.is_valid() and
            donoraddress_form.is_valid()):
            return self.form_valid(form, donoruser_form, donoraddress_form)
        else:
            return self.form_invalid(form, donoruser_form, donoraddress_form)

    def form_valid(self, form, donoruser_form, donoraddress_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        donoruser_form.instance = self.object
        donoruser_form.save()
        donoraddress_form.instance = self.object
        donoraddress_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, donoruser_form, donoraddress_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  donoruser_form=donoruser_form,
                                  donoraddress_form=donoraddress_form))
