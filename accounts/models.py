from django.db import models
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User

# Create your models here.
class Pickup(TimeStampedModel):
    delivery_id = models.CharField(max_length=100)

    cost = models.DecimalField(max_digits=6, decimal_places=2)

class Donor(TimeStampedModel):
    user = models.OneToOneField(User)
    history = models.ManyToManyField(Pickup)
