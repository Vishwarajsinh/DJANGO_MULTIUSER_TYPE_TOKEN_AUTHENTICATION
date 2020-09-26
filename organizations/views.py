from django.shortcuts import render
import django.http.request
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import *
# Create your views here.


class OrganizationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, HasOrganizationPermissions)

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class OrganizationLocationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, HasOrganizationLocationPermissions)

    queryset = OrganizationLocation.objects.all()
    serializer_class = OrganizationLocationSerializer


class LocationBranchViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, HasLocationBranchesPermissions)

    queryset = LocationBranch.objects.all()
    serializer_class = LocationBranchSerializer



