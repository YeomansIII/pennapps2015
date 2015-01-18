from django.contrib import admin
from app.models import DonationCenter, Address, Coordinate, Pickup

# Register your models here.
admin.site.register(DonationCenter)
admin.site.register(Address)
admin.site.register(Coordinate)
admin.site.register(Pickup)
