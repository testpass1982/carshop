from django.contrib import admin
from main.models import Car, CarBrand, CarProp, Company
from nested_admin import NestedModelAdmin, NestedStackedInline

# Register your models here.


class CarBrandInline(NestedStackedInline):
    model = CarBrand
    sortable_field_name = "ordering"
    extra = 0


class CarPropInline(NestedStackedInline):
    model = CarProp
    sortable_field_name = "ordering"
    extra = 0


class CarInline(NestedStackedInline):
    model = Car
    sortable_field_name = "ordering"
    extra = 0
    inlines = [CarPropInline]


@admin.register(Company)
class CompanyAdmin(NestedModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    inlines = [
        CarBrandInline,
        CarInline,
    ]


@admin.register(CarBrand)
class CarBrandAdmin(NestedModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]


@admin.register(Car)
class CarAdmin(NestedModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["id", "title"]
    inlines = [
        CarPropInline,
    ]


@admin.register(CarProp)
class CarPropertyAdmin(admin.ModelAdmin):
    list_display = ["id", "option", "value"]
    list_display_links = ["id", "option"]
