from urllib import response
from django.shortcuts import render
from rest_framework import views, status
from rest_framework.response import Response
from .models import *
from .serializers import *


    
class PQRType(views.APIView):
    serializer_class = PQRTypeSerializer

    def get(self,request):
        PQRTys = PQRTypes.objects.all()
        serializer = PQRTypeSerializer(PQRTys, many=True)
            
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'Nombre': request.data.get('Nombre')
        }

        serializer = PQRTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailPQRType(views.APIView):
    def get(self,request, id):
        try:
            PQRTy = PQRTypes.objects.filter(id=id)
        except PQRTypes.DoesNotExist:
            PQRTy = None
        if PQRTy:
            serializer = PQRTypeSerializer(PQRTy.get(),many=False)
        else:
            return Response({"res": f"El objeto con el id: {id} no existe"},status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self, request, id):
        try:
            PQRTy = PQRTypes.objects.get(id=id)
        except PQRTypes.DoesNotExist:
            PQRTy = None
        
        if not PQRTy:
            return Response({"res": f"El objeto con el id: {id} no existe"},status=status.HTTP_400_BAD_REQUEST)

        data = {
            'Nombre': request.data.get('Nombre')
        }

        serializer = PQRTypeSerializer(instance = PQRTy, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        
        try:
            PQRTy = PQRTypes.objects.get(id=id)
        except PQRTypes.DoesNotExist:
            PQRTy = None

        if not PQRTy:
            return Response({"res": f"El objeto con el id: {id} no existe"},status=status.HTTP_400_BAD_REQUEST)

        PQRTy.delete()
        return Response({"res": f"Tipo de PQR con id: {id} ha sido eliminado!"}, status=status.HTTP_200_OK)


class PQRS(views.APIView):
    serializer_class = PQRSerializer
    def get(self,request):
        AllPQR = PQR.objects.all()
        serializer = PQRSerializer(AllPQR, many=True)
            
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'IdNum': request.data.get('IdNum'),
            'IdType': request.data.get('IdType'),
            'Names': request.data.get('Names'),
            'LastNames': request.data.get('LastNames'),
            'Cellphone': request.data.get('Cellphone'),
            'Phone': request.data.get('Phone'),
            'Email': request.data.get('Email'),
            'Title': request.data.get('Title'),
            'TicketType': request.data.get('TicketType'),
            'Description': request.data.get('Description'),
            'Status': request.data.get('Status'),
        }

        serializer = PQRSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailPQR(views.APIView):
    def get(self,request, id):
        try:
            QueryPQR = PQR.objects.filter(id=id)
        except PQR.DoesNotExist:
            QueryPQR = None
            
        if QueryPQR:
            serializer = PQRSerializer(QueryPQR.get(),many=False)
        else:
            return Response({"res": f"El objeto con el id: {id} no existe"},status=status.HTTP_400_BAD_REQUEST)
            
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self, request, id):
        try:
            QueryPQR = PQR.objects.get(id=id)
        except PQR.DoesNotExist:
            QueryPQR = None
        
        if not QueryPQR:
            return Response({"res": f"El objeto con el id: {id} no existe"},status=status.HTTP_400_BAD_REQUEST)

        data = {
            'IdNum': request.data.get('IdNum'),
            'IdType': request.data.get('IdType'),
            'Names': request.data.get('Names'),
            'LastNames': request.data.get('LastNames'),
            'Cellphone': request.data.get('Cellphone'),
            'Phone': request.data.get('Phone'),
            'Email': request.data.get('Email'),
            'Title': request.data.get('Title'),
            'TicketType': request.data.get('TicketType'),
            'Description': request.data.get('Description'),
            'Status': request.data.get('Status'),
        }

        serializer = PQRSerializer(instance = QueryPQR, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        
        try:
            QueryPQR = PQR.objects.get(id=id)
        except PQR.DoesNotExist:
            QueryPQR = None
        
        if not QueryPQR:
            return Response({"res": f"El objeto con el id: {id} no existe"},status=status.HTTP_400_BAD_REQUEST)

        QueryPQR.delete()
        return Response({"res": f"Tipo de PQR con id: {id} ha sido eliminado!"}, status=status.HTTP_200_OK)

class DeletePQRS(views.APIView):
    def delete(self, request):
        list_id = request.data.get('ids')
        response = {}
        for id in list_id:
            QueryPQR = PQR.objects.filter(id=id)
            if not QueryPQR:
                response[id] = f"El objeto con el id: {id} no existe"
            else:
                response[id] = f"Tipo de PQR con id: {id} ha sido eliminado!"
                QueryPQR.get().delete()

        return Response({"res": response}, status=status.HTTP_200_OK)

class InfoPQRTypes(views.APIView):
    def get(self,request):
        dataPQRTypes = {
            'Nombre': "String",
        }
        data= {
            "Info": "A continuación se daran las apis donde se haran las peticiones para el modelo (Tipo de PQR)",
            "Listar" : "Metodo GET -> http://127.0.0.1:8000/api/pqrs/type/",
            "Registro TIPO PQR" : "Metodo POST -> http://127.0.0.1:8000/api/pqrs/type/ , Se recibiran los datos requeridos por medio del Body de la siguiente manera",
            "Estructura Registro" : dataPQRTypes,
            "Detalle Tipo PQR" : "Se recibe un parametro INT al final de la URL -> http://127.0.0.1:8000/api/pqrs/type/2/",
            "Actualizar Registro": "Metodo PUT -> EJ: http://127.0.0.1:8000/api/pqrs/type/2/ , Se recibiran los datos requeridos por medio del Body de la siguiente manera",
            "Estructura Actualizar": dataPQRTypes,
            "Eliminar Tipo PQR" : "Metodo DELETE -> EJ: http://127.0.0.1:8000/api/pqrs/type/2/"

        }
        return Response(data, status=status.HTTP_200_OK)

class InfoPQR(views.APIView):
    def get(self,request):
        dataPQRTypes = {
            'IdNum': "String",
            'IdType': "String Seleccionable ('CC','TI','CE')",
            'Names': "String",
            'LastNames': "String",
            'Cellphone': "PhoneNumberField Ej(+573224562174)",
            'Phone': "String (max_length=10)",
            'Email': "Email",
            'Title': "String",
            'TicketType': "Int (Foreign Key - PQR Type)",
            'Description': "String",
            'Status': "String Seleccionable ('abierto','cerrado')",
        }

        data= {
            "Info": "A continuación se daran las apis donde se haran las peticiones para el modelo (PQR)",
            "Listar" : "Metodo GET -> http://127.0.0.1:8000/api/pqrs/pqr/",
            "Registro PQR" : "Metodo POST -> http://127.0.0.1:8000/api/pqrs/pqr/ , Se recibiran los datos requeridos por medio del Body de la siguiente manera",
            "Estructura Registro" : dataPQRTypes,
            "Detalle PQR" : "Se recibe un parametro INT al final de la URL -> http://127.0.0.1:8000/api/pqrs/pqr/2/",
            "Actualizar Registro": "Metodo PUT -> EJ: http://127.0.0.1:8000/api/pqrs/pqr/2/ , Se recibiran los datos requeridos por medio del Body de la siguiente manera",
            "Estructura Actualizar": dataPQRTypes,
            "Eliminar PQR" : "Metodo DELETE -> EJ: http://127.0.0.1:8000/api/pqrs/pqr/2/"

        }
        return Response(data, status=status.HTTP_200_OK)

