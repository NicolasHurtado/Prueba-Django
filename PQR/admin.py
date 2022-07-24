from django.contrib import admin
from .models import PQR, PQRTypes

# Register your models here.
class PQRTypesAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)

class PQRAdmin(admin.ModelAdmin):
    list_display = ('IdNum', 'TicketType', 'Status', 'Created')


admin.site.register(PQRTypes, PQRTypesAdmin)
admin.site.register(PQR, PQRAdmin)

