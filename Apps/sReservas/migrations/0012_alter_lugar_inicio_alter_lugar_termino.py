# Generated by Django 4.1.3 on 2022-12-21 02:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sReservas', '0011_lugar_total_alter_lugar_termino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='inicio',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='termino',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
