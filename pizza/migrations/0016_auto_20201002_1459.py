# Generated by Django 3.1.1 on 2020-10-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0015_auto_20201002_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ingredients',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
