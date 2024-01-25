from django.contrib import admin
from .models import IncidentDown
# Register your models here.

class IncidentDownAdmin(admin.ModelAdmin):
        list_display = (
        'date',
        'name',
        'description',
    )
admin.site.register(IncidentDown, IncidentDownAdmin)