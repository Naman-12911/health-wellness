# Generated by Django 4.2.5 on 2023-10-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='photo_1',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_2',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_3',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_4',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_5',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_6',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo_main',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='video',
            field=models.URLField(blank=True),
        ),
    ]
