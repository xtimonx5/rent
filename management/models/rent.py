from django.db import models

from .customer import Customer
from .car import Car


class Rent(models.Model):
    STATUS_CHOICES = (
        ('Reserved', 'Reserved'),
        ('Rented', 'Rented'),
        ('Returned', 'Returned'),
    )

    car = models.ForeignKey(Car, related_name='rents')
    customer = models.ForeignKey(Customer)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50)
    comment = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.start_date) + '-' + str(self.end_date)

    class Meta:
        app_label = 'management'
