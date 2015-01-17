from django.db import models

# Create your models here.
class DonationCenter(models.Model):
    name = models.CharField(max_length=100)

    FOOD = 'fd'
    CLOTHING = 'cl'
    RAPP = 'ra'
    SHENANDOAH = 'sh'
    INDUSTRY_CHOICES = (
        (FOOD, 'Food'),
        (CLOTHING, 'Clothing'),
        (RAPP, 'Rappahannock'),
        (SHENANDOAH, 'Shenandoah'),
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

    longitude = models.CharField(max_length=9)
    latitude = models.CharField(max_length=9)

    def __str__(self):              # __unicode__ on Python 2
        return self.longitude+" "+self.latitude
