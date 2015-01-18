from django.db import models
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User
from app.models import Pickup, Address

# Create your models here.
class Delivery(TimeStampedModel):
    delivery_id = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    pickup = models.OneToOneField(Pickup)

class Donor(TimeStampedModel):
    user = models.OneToOneField(User)
    address = models.ForeignKey(Address)
    history = models.ManyToManyField(Delivery, blank=True)
    phone_number = models.CharField(max_length=20)
    business_name = models.CharField(max_length=100)
