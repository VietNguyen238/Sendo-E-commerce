# Generated by Django 5.0.2 on 2024-04-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_purchase_remove_product_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='purchase',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
