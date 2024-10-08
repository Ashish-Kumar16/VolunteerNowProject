# Generated by Django 5.0.7 on 2024-08-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opportunities', '0007_alter_organization_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteeropportunity',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='country',
            field=models.CharField(default='India', max_length=255),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='timezone',
            field=models.CharField(default='Asia/Calcutta', max_length=255),
        ),
        migrations.AddField(
            model_name='volunteeropportunity',
            name='zip_code',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
