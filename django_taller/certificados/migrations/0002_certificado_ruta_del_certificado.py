# Generated by Django 4.0.3 on 2022-03-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='ruta_del_certificado',
            field=models.CharField(default='', max_length=500),
        ),
    ]
