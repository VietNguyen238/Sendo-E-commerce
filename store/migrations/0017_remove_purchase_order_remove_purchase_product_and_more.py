# Generated by Django 5.0.2 on 2024-04-17 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='order',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='purchase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.purchase'),
        ),
    ]
