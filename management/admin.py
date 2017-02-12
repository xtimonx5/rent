from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    Car,
    Customer,
    Rent
)

from .admins import (
    CarAdmin,
    CustomerAdmin,
    RentAdmin,
)

admin.site.unregister(Group)

admin.site.register(Car, CarAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Rent, RentAdmin)
