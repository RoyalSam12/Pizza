# Generated by Django 3.1.1 on 2020-10-03 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0023_auto_20201003_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza_img',
            field=models.ImageField(height_field=619, null=True, upload_to='images', width_field=960),
        ),
    ]