# Generated by Django 3.2.14 on 2022-07-23 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PQR', '0002_alter_pqr_tickettype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqr',
            name='Phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Numero de telefono fijo'),
        ),
    ]