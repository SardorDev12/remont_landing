# landing_site/main/admin.py
from django.contrib import admin
from .models import Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone_number')
    search_fields = ('full_name',)

admin.site.register(Application, ApplicationAdmin)
