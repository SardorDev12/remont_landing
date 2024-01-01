# landing_site/main/admin.py
from django.contrib import admin
from .models import Application

admin.site.register(Application)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email')
