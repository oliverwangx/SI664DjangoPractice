from django.contrib import admin

# Register your models here.
from boats.models import Type, Boat

# Register your models here.

admin.site.register(Type)
admin.site.register(Boat)