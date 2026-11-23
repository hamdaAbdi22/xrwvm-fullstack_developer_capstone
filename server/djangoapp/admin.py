from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline: show car models inside the CarMake page
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1


# CarModelAdmin
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    list_filter = ['type', 'car_make', 'year']
    search_fields = ['name']


# CarMakeAdmin with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ['name', 'country', 'description']
    search_fields = ['name']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)