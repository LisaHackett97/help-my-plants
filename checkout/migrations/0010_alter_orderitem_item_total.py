# Generated by Django 3.2.9 on 2021-12-12 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_remove_order_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='item_total',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=6),
        ),
    ]
