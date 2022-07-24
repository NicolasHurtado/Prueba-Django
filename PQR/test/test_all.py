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
        PQR.objects.create(IdNum="1193587425",IdType="CC", Names="Andres Felipe", LastNames="Rojas Londoño", Cellphone="+57322478565", Phone="6024221021", Email="Andresrojas21@gmail.com", Title= "Prueba Test", TicketType_id=1, Description="PRUEBA TEST...", status="abierto")
        
    def test_get_all_pqr(self):
        response = client.get("/api/pqrs/pqr")
        print(response.json())
        