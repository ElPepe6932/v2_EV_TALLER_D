# Generated by Django 4.1.3 on 2022-12-20 01:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0002_remove_reserva_fecha_remove_reserva_horatermino'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ola', models.CharField(max_length=50)),
                ('inicio', models.DateField(null=True)),
                ('numero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.reserva')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.vehiculo')),
            ],
        ),
    ]