from django.contrib import admin
from .models import Category, Pizza, Ingredients, Price, Weight


class PriceInline(admin.TabularInline):
    model = Price


class IngredientsInline(admin.TabularInline):
    model = Pizza.ingredients.through


class WeightInline(admin.TabularInline):
    model = Weight


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



admin.site.register(Category, CategoryAdmin)

admin.site.register(Pizza, PizzaAdmin)

admin.site.register(Ingredients, IngredientsAdmin)
