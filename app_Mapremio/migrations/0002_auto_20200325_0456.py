# Generated by Django 3.0.4 on 2020-03-25 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Mapremio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medidasdeapremio',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='medidasdeapremio',
            name='nombres',
        ),
    ]