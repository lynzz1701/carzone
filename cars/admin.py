from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class carAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(obj.car_photo.url))
    
    thumbnail.short_description = 'Car Image'
    
    list_display = ('car_title', 'thumbnail', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured',)
    list_display_links = ('car_title',)
    list_editable = ('is_featured', )
    search_fields = ('car_title', 'city', 'model', 'body_style', 'fuel_type',)
    
    list_filter = ('city', 'model','body_style', 'fuel_type',)
    
admin.site.register(Car, carAdmin)