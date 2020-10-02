# Generated by Django 3.1.1 on 2020-09-30 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0002_auto_20200930_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.category'),
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_pizza_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('medium_pizza_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('large_pizza_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pizza', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pizza.pizza')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.CharField(max_length=20)),
                ('pizza', models.ManyToManyField(to='pizza.Pizza')),
            ],
        ),
    ]
