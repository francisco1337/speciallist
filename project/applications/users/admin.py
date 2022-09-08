from django.contrib import admin
from .models import User, Rol, Country, State, Town
# Register your models here.

admin.site.register(User)
admin.site.register(Rol)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Town)
