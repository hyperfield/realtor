# Generated by Django 2.2.4 on 2021-01-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0026_auto_20210119_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
    ]
