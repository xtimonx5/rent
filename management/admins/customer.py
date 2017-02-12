from django.contrib import admin
from django.utils.html import format_html
from ..models import Rent


class RentInline(admin.TabularInline):
    model = Rent
    extra = 0
    can_delete = False

    def has_add_permission(self, request):
        return False

    readonly_fields = (
        'car',
        'customer',
        'status',
        'comment',
    )


class CustomerAdmin(admin.ModelAdmin):
    inlines = (
        RentInline,
    )
