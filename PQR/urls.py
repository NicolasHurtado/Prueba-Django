from django.urls import path, include
from rest_framework import routers
from PQR.views import *

urlpatterns = [
    path("type/", PQRType.as_view(), name="PQRTypes"),
    path("type/<int:id>/", DetailPQRType.as_view(), name="DetailPQRTypes"),
    path("pqr/", PQRS.as_view(), name="PQRS"),
    path("pqr/<int:id>/", DetailPQR.as_view(), name="DetailPQRS"),
    path("delete_pqrs/", DeletePQRS.as_view(), name="delete_pqrs"),
    path("info_pqr_type/", InfoPQRTypes.as_view(), name="info_pqr_type"),
    path("info_pqr/", InfoPQR.as_view(), name="info_pqr"),
]
