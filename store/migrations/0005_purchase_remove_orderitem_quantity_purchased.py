# Generated by Django 5.0.2 on 2024-04-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_quantity_purchased_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_purchased', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity_purchased',
        ),
    ]