# Generated by Django 5.0.6 on 2024-06-04 22:41

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('body', models.CharField(max_length=300, verbose_name='Mensagem')),
                ('author', models.CharField(max_length=100)),
                ('grade', models.CharField(choices=[('R', 'Ruim'), ('B', 'Bom'), ('Mb', 'Muito bom')], max_length=20, verbose_name='Avaliação')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('body', models.CharField(max_length=300, verbose_name='Descrição')),
                ('profile_image', models.ImageField(upload_to='media/events/', verbose_name='Imagem de perfil')),
                ('begin_date', models.DateField(verbose_name='Data de início')),
                ('end_date', models.DateField(verbose_name='Data de fim')),
                ('time', models.TimeField(verbose_name='Horário')),
                ('address', models.CharField(max_length=100, verbose_name='Endereço')),
                ('location', models.CharField(max_length=100, verbose_name='Localização')),
                ('link', models.URLField(verbose_name='Link')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor')),
                ('pix_key', models.URLField(max_length=100, verbose_name='Chave PIX')),
                ('pix_key_owner', models.CharField(max_length=100, verbose_name='Dono da chave PIX')),
                ('bank_name', models.CharField(max_length=100, verbose_name='Banco')),
                ('pdf_link', models.URLField(max_length=100, null=True, verbose_name='Link para PDF')),
                ('questionary_link', models.URLField(max_length=100, null=True, verbose_name='Link para questionário')),
                ('category', models.CharField(choices=[('F', 'Feira'), ('Ft', 'Festividade'), ('Cl', 'Celebração')], default='Vazio', max_length=20)),
                ('format', models.CharField(choices=[('P', 'Presencial'), ('V', 'Virtual'), ('H', 'Híbrido')], default='Vazio', max_length=20)),
                ('fk_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_app.project', verbose_name='Associado ao projeto')),
            ],
        ),
    ]
