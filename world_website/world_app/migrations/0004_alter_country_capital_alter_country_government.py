# Generated by Django 5.0.1 on 2024-01-04 21:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_app', '0003_alter_continent_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='world_app.city'),
        ),
        migrations.AlterField(
            model_name='country',
            name='government',
            field=models.CharField(blank=True, choices=[('Democracy', 'Democracy'), ('Republic', 'Republic'), ('Monarchy', 'Monarchy'), ('Communism', 'Communism'), ('Dictatorship', 'Dictatorship')], default='democracy', max_length=100, null=True),
        ),
    ]