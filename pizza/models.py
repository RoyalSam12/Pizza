from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
