# Generated by Django 3.1.1 on 2020-10-02 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0010_auto_20201002_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredients',
            options={'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
    ]
