# Generated by Django 5.0.7 on 2024-08-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0003_alter_organization_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(max_length=100, verbose_name='City'),
        ),
    ]
