# Generated by Django 2.2.4 on 2021-01-16 18:28
# from ..models import Flat

from django.db import migrations
import phonenumbers


def transfer_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            parsed_phone = phonenumbers.parse(flat.owners_phonenumber, None)
            flat.owner_pure_phone = parsed_phone
            flat.save()
        except phonenumbers.phonenumberutil.NumberParseException:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0012_auto_20210116_2053'),
    ]

    operations = [migrations.RunPython(transfer_phone_numbers),
    ]
