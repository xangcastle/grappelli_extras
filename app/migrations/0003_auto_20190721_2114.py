# Generated by Django 2.1.1 on 2019-07-21 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190721_2104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Customer',
        ),
    ]
