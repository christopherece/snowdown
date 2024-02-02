from django.contrib import admin
from .models import IncidentDown
# Register your models here.

class IncidentDownAdmin(admin.ModelAdmin):
        list_display = (
        'name',
        'description',
        'date',
    )
admin.site.register(IncidentDown, IncidentDownAdmin)