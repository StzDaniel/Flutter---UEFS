# Generated by Django 5.0.6 on 2024-05-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
