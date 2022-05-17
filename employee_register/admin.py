from django.contrib import admin
from .models import Employee, Department, Position

# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)
admin.site.register(Department)
