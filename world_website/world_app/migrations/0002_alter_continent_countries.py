# Generated by Django 5.0.1 on 2024-01-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='countries',
            field=models.ManyToManyField(blank=True, null=True, related_name='continents', to='world_app.country'),
        ),
    ]
