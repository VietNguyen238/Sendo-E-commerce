# Generated by Django 5.0.2 on 2024-04-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_quantity_purchased'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_purchased',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity_purchased',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
