# Generated by Django 4.2 on 2023-11-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0017_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
