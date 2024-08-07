from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_name', 'departments_id', 'information')
    search_fields = ('doctor_name', 'departments_id__departments_name')

    fieldsets = (
        (None, {
            'fields': ('doctor_name', 'departments_id', 'information')
        }),
    )