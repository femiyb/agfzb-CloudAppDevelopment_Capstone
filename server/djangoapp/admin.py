from django.contrib import admin
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):  # or admin.StackedInline
    model = CarModel
    extra = 1  # Number of empty CarModel forms to display

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
