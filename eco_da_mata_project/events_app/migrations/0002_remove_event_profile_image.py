# Generated by Django 5.0.6 on 2024-06-05 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='profile_image',
        ),
    ]
