# Generated by Django 4.1 on 2022-11-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0003_tabla_posiciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabla_posiciones',
            name='diferencia',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tabla_posiciones',
            name='escudo_equipo',
            field=models.ImageField(null=True, upload_to='static/imagenes/equipos/escudos/', verbose_name='Escudo equipo'),
        ),
    ]
