from django.db import models

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
        return self.num+" "+self.street

class Coordinate(models.Model):

    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)

    def __str__(self):              # __unicode__ on Python 2
        return self.longitude+" "+self.latitude
