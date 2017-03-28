from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import DateFieldListFilter
from django.contrib.admin import SimpleListFilter
from management.models import Car
import datetime
from django.contrib import messages


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'make',
        'model',
        'year',
        'status',
    )
    search_fields = ('rents__start_date',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(CarAdmin, self).get_search_results(request, queryset, search_term)
        if not use_distinct:
            return queryset, use_distinct
        else:
            if validate(search_term):
                qs = Car.objects.all().exclude(rents__start_date__lte=search_term, rents__end_date__gte=search_term)
                return qs, use_distinct
            else:
                messages.add_message(request, messages.ERROR, 'Try YYYY-MM-DD format date')
                return queryset, use_distinct

    fields = (
        'make',
        'model',
        'year',
        'engine',
        'photo',
        'status',
        'cost',
        'auto_number'
    )
