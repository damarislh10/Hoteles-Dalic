# Generated by Django 3.2.8 on 2021-10-08 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='ubicación',
            new_name='ubicacion',
        ),
    ]
