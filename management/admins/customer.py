from django.contrib import admin
from django.utils.html import format_html
from ..models import Rent


class RentInline(admin.TabularInline):
    model = Rent
    extra = 0
    can_delete = False
    can_add = False


    def has_add_permission(self, request):
        return False

    def has_module_permission(self, request):
        return True


    readonly_fields = (
        'car',
        'customer',
        'status',
        'comment',
        'address'
    )

    verbose_name = 'History of activity'
    verbose_name_plural = 'History of activity'


class CustomerAdmin(admin.ModelAdmin):
    inlines = (
        RentInline,
    )
