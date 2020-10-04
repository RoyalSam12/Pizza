from django.contrib import admin
from .models import (
    Category, Pizza,
    Ingredients, Price,
    Weight, BeveragesCategory,
    Beverages, BeveragesPrice,
    BeveragesWeight

)


class PriceInline(admin.TabularInline):
    model = Price


class IngredientsInline(admin.TabularInline):
    model = Pizza.ingredients.through


class WeightInline(admin.TabularInline):
    model = Weight


class BeveragesWeightInline(admin.TabularInline):
    model = BeveragesWeight


class BeveragesPriceInline(admin.TabularInline):
    model = BeveragesPrice


class PizzaInline(admin.TabularInline):
    model = Pizza
    exclude = ('ingredients',)


class PizzaAdmin(admin.ModelAdmin):
    model = Pizza
    inlines = [
        WeightInline,
        IngredientsInline
    ]
    exclude = ('ingredients',)


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [
        PizzaInline,
        PriceInline
    ]
    exclude = ('ingredients',)


class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredients


class BeveragesInLine(admin.TabularInline):
    model = Beverages
    exclude = ('drink_img',)


class BeveragesAdmin(admin.ModelAdmin):
    model = Beverages
    inlines = [
        BeveragesWeightInline,
        BeveragesPriceInline
    ]


class BeveragesCategoryAdmin(admin.ModelAdmin):
    model = BeveragesCategory
    inlines = [
        BeveragesInLine,
    ]




admin.site.register(Category, CategoryAdmin)

admin.site.register(Pizza, PizzaAdmin)

admin.site.register(Ingredients, IngredientsAdmin)

admin.site.register(BeveragesCategory, BeveragesCategoryAdmin)

admin.site.register(Beverages, BeveragesAdmin)
