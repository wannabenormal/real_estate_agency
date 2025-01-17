# Generated by Django 2.2.24 on 2022-02-15 15:52

from django.db import migrations


def create_owners_from_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            name=flat.owner,
            phone_number=flat.owners_phonenumber,
            defaults={
                'pure_phone_number': flat.owner_pure_phone,
            }
        )

        owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(create_owners_from_flats)
    ]
