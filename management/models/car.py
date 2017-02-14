from django.db import models


class Car(models.Model):
    STATUS_CHOICES = (
        ('Good state', 'Good state'),
        ('Broken', 'Broken')
    )

    make = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    engine = models.CharField(max_length=50, null=True, blank=True)
    photo = models.FileField(null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    cost = models.CharField(max_length=50,default='100$', null=True, blank=True)
    auto_number = models.CharField(max_length=50,default='', null=True, blank=True)


    def __str__(self):
        return self.make + ' ' + self.model + ' ' + str(self.pk)

    class Meta:
        app_label = 'management'
