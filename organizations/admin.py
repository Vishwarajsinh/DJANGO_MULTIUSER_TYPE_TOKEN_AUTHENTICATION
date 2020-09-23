from django.contrib import admin
from .models import *

# super admin id-password
# books -> admin@123
# admin -> admin@123


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'org_name',
        'mailing_name',
        'website_url',
        'GST_status',
        'PAN',
        'GSTIN',
        'prevyear_annual_turnover',
        'finance_year',
        'CIN',
    )

class OrganizationLocationAdmin(admin.ModelAdmin):
    list_display = (

    )

class LocationBranchAdmin(admin.ModelAdmin):
    list_display = (

    )

# Register your models here.
admin.site.register( Organization, OrganizationAdmin ),
admin.site.register( OrganizationLocation, OrganizationLocationAdmin ),
admin.site.register( LocationBranch, LocationBranchAdmin ),