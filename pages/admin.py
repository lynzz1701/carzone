from django.contrib import admin
from .models import teamMember
from django.utils.html import format_html

# Register your models here.

class teamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(obj.photo.url))
    
    thumbnail.short_description = 'Photo'
    
    list_display = ('thumbnail', 'last_name', 'designation', 'created_date',)
    list_display_links = ('last_name',)
    search_fields = ('first_name', 'last_name', 'designation',)
    
    list_filter = ('designation',)
admin.site.register(teamMember, teamAdmin)