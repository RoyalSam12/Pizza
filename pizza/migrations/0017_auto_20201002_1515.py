# Generated by Django 3.1.1 on 2020-10-02 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0016_auto_20201002_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredients',
            options={'ordering': ('ingredients',), 'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
    ]
