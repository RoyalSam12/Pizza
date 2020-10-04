from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Ingredients(models.Model):
    ingredients = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'
        ordering = ('ingredients',)

    def __str__(self):
        return self.ingredients


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=30)
    pizza_img = models.ImageField(upload_to='images', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredients)

    class Meta:
        ordering = ('category', 'pizza_name')

    def __str__(self):
        return self.pizza_name


class Price(models.Model):
    small_pizza_price = models.DecimalField(max_digits=5, decimal_places=2)
    medium_pizza_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_pizza_price = models.DecimalField(max_digits=5, decimal_places=2)
    pizza = models.OneToOneField(Category, on_delete=models.CASCADE)


class Weight(models.Model):
    small_pizza_weight = models.IntegerField(default=0)
    medium_pizza_weight = models.IntegerField(default=0)
    large_pizza_weight = models.IntegerField(default=0)
    pizza = models.OneToOneField(Pizza, on_delete=models.CASCADE)


class BeveragesCategory(models.Model):
    category_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Beverages Categories'

    def __str__(self):
        return self.category_name


class BeveragesWeight(models.Model):
    weight = models.IntegerField(default=0, unique=True)

    class Meta:
        ordering = ('weight',)

    def __str__(self):
        return str(self.weight)


class BeveragesPrice(models.Model):
    price = models.IntegerField(default=0, unique=True)

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return str(self.price)


class Beverages(models.Model):
    drink_name = models.CharField(max_length=50)
    drink_img = models.ImageField(upload_to='images_drinks_beverages', null=True)
    category = models.ForeignKey(BeveragesCategory, on_delete=models.CASCADE)
    price = models.ManyToManyField(BeveragesPrice)
    weight = models.ManyToManyField(BeveragesWeight)

    class Meta:
        verbose_name_plural = 'Beverages'

    def __str__(self):
        return self.drink_name
