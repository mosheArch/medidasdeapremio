# Generated by Django 3.0.4 on 2020-03-26 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_Mapremio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediosImpugnacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_expediente', models.CharField(max_length=255, unique=True)),
                ('fecha_emplazamiento', models.DateField()),
                ('tipo_medioImpugnacion', models.CharField(choices=[('Juicio de amparo', 'Juicio de amparo'), ('Juicio administrativo', 'Juicio administrativo')], default='Tipo', max_length=255)),
                ('efecto_medioImpugnacion', models.TextField(max_length=255)),
                ('comentarios', models.TextField(max_length=255, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('medidas_apremio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Mapremio.MedidasdeApremio')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
