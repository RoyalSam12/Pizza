from django.shortcuts import render

from .models import Category, Pizza


def index(requests):
    context = {
        'category': Category.objects.all(),
        'pizza': Pizza.objects.all()
    }
    return render(requests, 'pizza/index.html', context=context)
