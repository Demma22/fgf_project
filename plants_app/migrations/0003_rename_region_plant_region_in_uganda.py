# Generated by Django 4.2.5 on 2023-10-11 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants_app', '0002_remove_plant_languages_plant_botanical_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='region',
            new_name='region_in_Uganda',
        ),
    ]
