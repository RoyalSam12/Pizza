# Generated by Django 3.1.1 on 2020-10-02 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0014_auto_20201002_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='medium_pizza_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
