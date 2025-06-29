# Generated by Django 5.2.3 on 2025-06-12 00:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('toyota', 'Toyota'), ('honda', 'Honda'), ('nissan', 'Nissan')], max_length=30)),
                ('model', models.CharField(max_length=40)),
                ('year', models.PositiveIntegerField()),
                ('mileage_km', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(choices=[('gasolina', 'Gasolina'), ('diesel', 'Diésel'), ('hibrido', 'Híbrido'), ('electrico', 'Eléctrico')], max_length=10)),
                ('price_clp', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
