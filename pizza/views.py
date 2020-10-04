from django.shortcuts import render

from .models import Category, BeveragesCategory


def index(requests):
    context = {
        'category': Category.objects.all(),
    }
    return render(requests, 'pizza/index.html', context=context)


def beverages(requests):
    context = {
        'category': BeveragesCategory.objects.all(),
    }
    return render(requests, 'pizza/beverages.html', context=context)

