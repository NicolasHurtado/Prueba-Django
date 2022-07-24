from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class PQRTypes(models.Model):
    Nombre = models.CharField(max_length=100, verbose_name="Nombre del PQR")

    class Meta:
        db_table = "PQRTypes"
        verbose_name_plural = "PQRTypes"

    def __str__(self):
        return self.Nombre




class PQR(models.Model):
    IdentificationTypes = [
        ('CC', 'Cedula de Ciudadania'),
        ('TI', 'Tarjeta de identidad'),
        ('CE', 'Cedula de extranjeria')
    ]


    StatusTicket = [
        ('abierto', 'abierto'),
        ('cerrado', 'cerrado')
    ]

    IdNum = models.CharField(max_length=100, verbose_name="Numero de identificación")
    IdType = models.CharField(max_length=100, choices=IdentificationTypes, verbose_name="Tipo de identificacón")
    Names = models.CharField(max_length=100, verbose_name="Nombres del cliente")
    LastNames = models.CharField(max_length=100, verbose_name="Apellidos del cliente")
    Cellphone = PhoneNumberField(null = True, blank = True, verbose_name="Numero de celular")
    Phone = models.CharField(max_length=10,null = True, blank=True, verbose_name='Numero de telefono fijo')
    Email = models.EmailField(max_length=200, verbose_name="Correo")
    Title =  models.CharField(max_length=200, verbose_name="Titulo del PQR")
    TicketType = models.ForeignKey(PQRTypes, on_delete=models.CASCADE, verbose_name="Tipo de Ticket")
    Description = models.TextField(max_length=1000, verbose_name="Descripción del Ticket")
    Status = models.CharField(max_length=7, choices=StatusTicket, verbose_name="Estado del Ticket")
    Created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        db_table = "PQR"
        verbose_name_plural = "PQR"

    def __str__(self):
        return self.IdNum