from ..models import Rent
from django.contrib import admin


class ActiveRentProxy(Rent):
    def __str__(self):
        return str(self.start_date) + '-' + str(self.end_date)

    class Meta:
        proxy=True
        verbose_name = 'Active rent'


class ActiveRentModelAdmin(admin.ModelAdmin):
    def car_info(self, instance):
        car = instance.car
        if car:
            return str(car.pk) + ' ' + car.make + \
                   ' ' + car.model + ' ' + str(car.year) + \
                   ' ' + car.engine

    def customer_info(self, instance):
        customer = instance.customer
        if customer:
            return customer.first_name + ' ' + customer.last_name + ' ' + customer.phone
    list_filter = ('start_date', 'end_date',)

    list_display = (
        # 'pk',
        'status',
        'customer_info',
        'car_info',
        'start_date',
        'end_date'
    )
    def get_queryset(self, request):
        return Rent.objects.all().exclude(status='Returned')