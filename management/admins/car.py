from django.contrib import admin
from django.utils.html import format_html


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

    list_filter = ('status',)

    fields = (
        'make',
        'model',
        'year',
        'engine',
        'current_image',
        'photo',
        'status'
    )

    readonly_fields = ('current_image',)
