from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("email","username")

class OnwerAdmin(admin.ModelAdmin):
    list_display = ("email","username","company_name","GST","PAN")

class ExecutiveAdmin(admin.ModelAdmin):
    list_display = ("email","username","designation","department")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("email","username", "role","department")



admin.site.register(User)
admin.site.register(Owner, OnwerAdmin)
admin.site.register(Executive, ExecutiveAdmin)
admin.site.register(Employee, EmployeeAdmin)
