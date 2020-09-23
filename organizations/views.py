from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.
class OrganizationViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationLocationViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = OrganizationLocation.objects.all()
    serializer_class = OrganizationLocationSerializer


class LocationBranchViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)

    queryset = LocationBranch.objects.all()
    serializer_class = LocationBranchSerializer
