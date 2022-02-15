# Generated by Django 2.2.24 on 2022-02-15 15:12

import phonenumbers
from django.db import migrations


def set_normalized_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')

        if not phonenumbers.is_valid_number(phone_number):
            continue

        flat.owner_pure_phone = phone_number
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(set_normalized_phone_numbers)
    ]
