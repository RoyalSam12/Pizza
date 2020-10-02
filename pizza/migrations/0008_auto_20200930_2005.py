# Generated by Django 3.1.1 on 2020-09-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0007_auto_20200930_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='large_pizza_weight',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='price',
            name='medium_pizza_weight',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='price',
            name='small_pizza_weight',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]