# Generated by Django 4.1.5 on 2023-01-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantdb', '0002_employee_employee_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(default=None, max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
