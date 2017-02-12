from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

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

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Rent site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')

admin_site = MyAdminSite()



# admin_site.unregister(Group)
admin_site.register(User)

admin_site.register(Car, CarAdmin)
admin_site.register(Customer, CustomerAdmin)
admin_site.register(Rent, RentAdmin)
