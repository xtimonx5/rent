from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin import DateFieldListFilter
from django.contrib.admin import SimpleListFilter
from management.models import Car


class CarAdmin(admin.ModelAdmin):
    def current_image(self, instance):
        image = instance.photo
        if image:
            return format_html(
                u'<img src="/static/attachments/%s" width = "500px" object-fit: contain; />' % image)
        else:
            return None

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
            qs = Car.objects.all().exclude(rents__start_date__lte=search_term, rents__end_date__gte=search_term)
            return qs,use_distinct

    fields = (
        'make',
        'model',
        'year',
        'engine',
        'current_image',
        'photo',
        'status',
        'cost',
        'auto_number'
    )

    readonly_fields = ('current_image',)
