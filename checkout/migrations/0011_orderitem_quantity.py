# Generated by Django 3.2.9 on 2021-12-12 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0010_alter_orderitem_item_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]