# Generated by Django 3.2.14 on 2022-07-23 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PQR', '0005_alter_pqr_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='PQRTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre del PQR')),
            ],
            options={
                'verbose_name_plural': 'PQRTypes',
                'db_table': 'PQRTypes',
            },
        ),
        migrations.AlterField(
            model_name='pqr',
            name='TicketType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PQR.pqrtypes', verbose_name='Tipo de Ticket'),
        ),
    ]
