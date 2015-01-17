from django.contrib import admin
from app.models import DonationCenter, Address, Coordinate

# Register your models here.
admin.site.register(DonationCenter)
admin.site.register(Address)
admin.site.register(Coordinate)
