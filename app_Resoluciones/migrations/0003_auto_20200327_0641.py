# Generated by Django 3.0.4 on 2020-03-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Resoluciones', '0002_auto_20200326_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resoluciones',
            name='multa',
            field=models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=10),
        ),
    ]
