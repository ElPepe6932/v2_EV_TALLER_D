# Generated by Django 4.1.3 on 2022-12-20 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginApp', '0002_remove_reserva_fecha_remove_reserva_horatermino'),
        ('sReservas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lugar',
            name='ola',
        ),
        migrations.AlterField(
            model_name='lugar',
            name='numero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.estacionamiento'),
        ),
    ]