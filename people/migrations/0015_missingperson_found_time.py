# Generated by Django 4.0.4 on 2022-05-26 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0014_rename_last_seen_reportedperson_reported_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='found_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
