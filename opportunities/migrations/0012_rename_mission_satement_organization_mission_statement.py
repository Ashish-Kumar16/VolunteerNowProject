# Generated by Django 5.0.7 on 2024-08-17 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0011_alter_organization_mission_satement_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organization',
            old_name='mission_satement',
            new_name='mission_statement',
        ),
    ]
