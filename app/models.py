from django.db import models

# Create your models here.
class DonationCenter(TimeStampedModel):
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
    default=NONE)

    address = models.ForeignKey('Address')
    coordinate = models.ForeignKey('Coordinate')

    def __str__(self):              # __unicode__ on Python 2
        return self.name
    def __unicode__(self):              # __unicode__ on Python 2
        return unicode(self.name)

class Address(TimeStampedModel):

    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    zip_code = models.IntegerField(max_length=5)

    def __str__(self):              # __unicode__ on Python 2
        return self.street
