# Generated by Django 3.2.9 on 2021-11-30 08:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='time_slot',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
