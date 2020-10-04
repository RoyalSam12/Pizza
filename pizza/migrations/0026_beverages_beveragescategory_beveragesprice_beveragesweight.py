# Generated by Django 3.1.1 on 2020-10-04 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0025_auto_20201003_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beverages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=30)),
                ('drink_img', models.ImageField(null=True, upload_to='images_drinks_beverages')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.category')),
            ],
        ),
        migrations.CreateModel(
            name='BeveragesCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='BeveragesWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('little_weight', models.IntegerField(blank=True)),
                ('medium_weight', models.IntegerField(blank=True)),
                ('big_weight', models.IntegerField(blank=True)),
                ('beverages', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pizza.beverages')),
            ],
        ),
        migrations.CreateModel(
            name='BeveragesPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('little_beverages', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('medium_beverages', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('big_beverages', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('beverages', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pizza.beverages')),
            ],
        ),
    ]