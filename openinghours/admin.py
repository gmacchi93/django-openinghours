# -*- coding: utf-8 -*-
from django.contrib import admin
from openinghours.models import OpeningHours, Company
from openinghours.app_settings import PREMISES_MODEL


class OpeningHoursInline(admin.TabularInline):
    model = OpeningHours
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    inlines = [OpeningHoursInline]
    search_fields = ['name', 'slug']

# OPENINGHOURS_PREMISES_MODEL users need to register
# their own admin from their app
if PREMISES_MODEL == 'openinghours.Company':
    admin.site.register(Company, CompanyAdmin)
