from django.contrib import admin

from .models import City, Client, Product, Provider


class CityInline(admin.StackedInline):
    model = City
    extra = 0


admin.site.register(City)
admin.site.register(Product)
admin.site.register(Provider)
admin.site.register(Client)
