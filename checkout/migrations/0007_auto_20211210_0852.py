# Generated by Django 3.2.9 on 2021-12-10 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20211209_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='original_cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='stripe_pid',
        ),
    ]
