# Generated by Django 3.1.1 on 2020-10-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0020_pizza_pizza_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza_img',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
