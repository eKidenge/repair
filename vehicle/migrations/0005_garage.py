# Generated by Django 5.1.4 on 2025-02-06 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_vehicle_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=50)),
                ('mechanic', models.CharField(max_length=100)),
            ],
        ),
    ]
