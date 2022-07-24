from rest_framework import serializers
from .models import *

class PQRTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQRTypes
        fields = '__all__'

class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQR
        fields = '__all__'
        #fields = ["IdNum", "IdType", "Names", "LastNames", "Cellphone", "Phone", "Email", "Title", "TicketType", "Description", "Status", "Created"]