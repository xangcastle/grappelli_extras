# Generated by Django 2.1.1 on 2019-07-21 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190721_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='country',
        ),
    ]
