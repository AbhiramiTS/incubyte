# Generated by Django 3.2 on 2021-09-04 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Last_Consulted_Date',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Open_Date',
            field=models.CharField(max_length=200, null=True),
        ),
    ]