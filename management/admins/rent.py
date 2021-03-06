from django.contrib import admin
from django.utils.html import format_html


class RentAdmin(admin.ModelAdmin):
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

    list_display = (
        'status',
        'customer_info',
        'car_info',
        'start_date',
        'end_date'
    )

    list_filter = (
        'status',
        'start_date',
        'end_date',
    )
    fields = (
        'car',
        'car_info',
        'customer',
        'customer_info',
        'status',
        'comment',
        'start_date',
        'end_date',
    )
    readonly_fields = (
        'car_info',
        'customer_info',
    )
