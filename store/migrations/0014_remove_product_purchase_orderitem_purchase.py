# Generated by Django 5.0.2 on 2024-04-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_product_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='purchase',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='purchase',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
