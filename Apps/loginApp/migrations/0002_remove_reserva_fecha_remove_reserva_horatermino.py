# Generated by Django 4.1 on 2022-12-19 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reserva',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='horaTermino',
        ),
    ]
