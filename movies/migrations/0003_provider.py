# Generated by Django 5.1.1 on 2024-09-30 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('movie', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='movies.movie')),
                ('service', models.CharField(blank=True, max_length=255)),
                ('has_flat_price', models.BooleanField(default=False)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
    ]
