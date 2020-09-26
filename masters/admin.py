from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Good)
admin.site.register(Service)
admin.site.register(Unit)
admin.site.register(UnitGroup)
admin.site.register(Supplier)
admin.site.register(Customer)