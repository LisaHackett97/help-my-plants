# Generated by Django 3.2.9 on 2021-12-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20211201_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='item_total',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=6),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_slot',
            field=models.DateField(blank=True, null=True),
        ),
    ]
