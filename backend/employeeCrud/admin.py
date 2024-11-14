from django.contrib import admin
from .models import Employee, Phone, Email

# Register your models here.
admin.site.register(Employee)
admin.site.register(Phone)
admin.site.register(Email)
