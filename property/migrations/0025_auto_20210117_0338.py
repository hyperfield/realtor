# Generated by Django 2.2.4 on 2021-01-17 00:38

from django.db import migrations


def assign_flats_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for owner in Owner.objects.all():
        flats = Flat.objects.filter(owner=owner.owner)
        owner.owned_flats.set(flats)
        owner.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0020_auto_20210117_0122'),
    ]

    operations = [migrations.RunPython(assign_flats_owners),
    ]