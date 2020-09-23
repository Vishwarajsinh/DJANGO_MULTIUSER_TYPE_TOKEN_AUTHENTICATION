from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class OrganizationLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationLocation
        fields = '__all__'

class LocationBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationBranch
        fields = '__all__'