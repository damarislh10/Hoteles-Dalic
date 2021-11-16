# Generated by Django 3.2.8 on 2021-10-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0004_remove_hotel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='calificacion',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='nombreHotel',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='precio',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='ubicacion',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
