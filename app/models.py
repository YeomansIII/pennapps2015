from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class DonationCenter(models.Model):
    name = models.CharField(max_length=100)

    FOOD = 'fd'
    CLOTHING = 'cl'
    TOYS = 'ty'
    HOUSEHOLD_ITEMS = 'hi'
    INDUSTRY_CHOICES = (
        (FOOD, 'Food'),
        (CLOTHING, 'Clothing'),
        (TOYS, 'Toys'),
        (HOUSEHOLD_ITEMS, 'Household Items'),
    )

    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES,
    default=FOOD)

    address = models.ForeignKey('Address')
    coordinate = models.ForeignKey('Coordinate')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)

class Address(models.Model):
    num = models.IntegerField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.num)+" "+self.street

class Coordinate(models.Model):

    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):              # __unicode__ on Python 2
        return str(self.longitude)+" "+str(self.latitude)

class Pickup(TimeStampedModel):
    manifest = models.CharField(max_length=100)
    pickup_name = models.CharField(max_length=100)
    pickup_address = models.CharField(max_length=100)
    pickup_phone_number = models.CharField(max_length=20)
    pickup_business_name = models.CharField(max_length=100)
    pickup_notes = models.CharField(max_length=200)
    dropoff = models.ForeignKey(DonationCenter)
    dropoff_notes = models.CharField(max_length=200)
    quote_id = models.CharField(max_length=20)

    def __str__(self):
        return self.manifest
