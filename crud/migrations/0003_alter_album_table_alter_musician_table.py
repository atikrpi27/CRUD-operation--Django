# Generated by Django 4.0.2 on 2022-02-06 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_album'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='album',
            table='Album',
        ),
        migrations.AlterModelTable(
            name='musician',
            table='Musician',
        ),
    ]
