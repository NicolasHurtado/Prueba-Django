# Generated by Django 3.2.14 on 2022-07-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PQR', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='TicketType',
            field=models.CharField(choices=[('peticion', 'peticion'), ('queja', 'queja'), ('reclamo', 'reclamo'), ('sugerencia', 'sugerencia')], max_length=10, verbose_name='Tipo de Ticket'),
        ),
    ]
