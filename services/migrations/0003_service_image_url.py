# Generated by Django 3.2.9 on 2021-11-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20211128_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
