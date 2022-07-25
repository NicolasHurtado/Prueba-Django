from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase
from PQR.models import *
import json
import os

client = APIClient()


class TestAll(TestCase):
    """Test module for GET all puppies API"""

    def setUp(self):
        PQRTypes.objects.create(Nombre="Prueba")
        PQR.objects.create(IdNum="1193587425",IdType="CC", Names="Andres Felipe", LastNames="Rojas Londoño", Cellphone="+57322478565", Phone="6024221021", Email="Andresrojas21@gmail.com", Title= "Prueba Test", TicketType_id=1, Description="PRUEBA TEST...", Status="abierto")
        
    def test_get_all_pqr(self):
        response = client.get("/api/pqrs/pqr/")
        assert len(response.json())==1
    
    def test_get_pqr(self):
        response = client.get("/api/pqrs/pqr/1/")
        assert response.json().get("IdNum") == "1193587425"
    
    def test_get_not_pqr(self):
        response = client.get("/api/pqrs/pqr/1000/")
        assert response.json().get("res") == 'El objeto con el id: 1000 no existe'

    def test_create_pqr_not_type(self):
        data = {
            "IdNum": "1193425698",
            "IdType": "CC",
            "Names": "Luis Felipe",
            "LastNames": "Ordoñez Escobar",
            "Cellphone": "+573202457899",
            "Phone": "6024523365",
            "Email": "felibien2002@gmail.com",
            "Title": "PRUEBA #3",
            "TicketType": 3,
            "Description": "PROBANDO POR TERCERA VEZ",
            "Status": "abierto"
        }
        response = client.post("/api/pqrs/pqr/", data=data)
        assert response.json().get('TicketType')[0] == 'Invalid pk "3" - object does not exist.'
    
    def test_update_pqr_not_found(self):
        data = {
            "IdNum": "1193425698",
            "IdType": "CC",
            "Names": "Luis Felipe",
            "LastNames": "Ordoñez Escobar",
            "Cellphone": "+573202457899",
            "Phone": "6024523365",
            "Email": "felibien2002@gmail.com",
            "Title": "PRUEBA #3",
            "TicketType": 1,
            "Description": "PROBANDO POR TERCERA VEZ",
            "Status": "abierto"
        }
        response = client.put("/api/pqrs/pqr/2/", data=data)
        assert response.json().get('res') == 'El objeto con el id: 2 no existe'

    def test_delete_pqr_type(self):
        response = client.delete("/api/pqrs/type/1/")
        assert response.json().get('res') == 'Tipo de PQR con id: 1 ha sido eliminado!'
    
    def test_delete_pqr_type_not_found(self):
        response = client.delete("/api/pqrs/type/1000/")
        assert response.json().get('res') == 'El objeto con el id: 1000 no existe'

    def test_get_all_pqr_type(self):
        response = client.get("/api/pqrs/type/")
        assert len(response.json())==1
    
    def test_get_pqr_type(self):
        response = client.get("/api/pqrs/type/1/")
        assert response.json().get("Nombre") == "Prueba"
    
    def test_get_not_pqr_type(self):
        response = client.get("/api/pqrs/type/1000/")
        assert response.json().get("res") == 'El objeto con el id: 1000 no existe'
    
    