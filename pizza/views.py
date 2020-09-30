from django.shortcuts import render


def index(requests):
    return render(requests, 'pizza/index.html')
