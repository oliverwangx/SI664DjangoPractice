from django.contrib import admin

# Register your models here.
from autos.models import Make, Auto

# Register your models here.

admin.site.register(Make)
admin.site.register(Auto)