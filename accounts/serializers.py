from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from django.shortcuts import HttpResponse

import json

class OwnerRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Owner
        fields = (
            'email',
            'username',
            'company_name',
            'GST',
            'PAN',
            'password',
            'password2'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        owner = Owner(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            company_name = self.validated_data['company_name'],
            GST = self.validated_data['GST'],
            PAN = self.validated_data['PAN']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password == password2:
            owner.set_password(password)
            owner.save()
            return owner
        else:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        

class ExecutiveRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Executive
        fields = (
            'email',
            'username',
            'designation',
            'department',
            'password',
            'password2'
        )
        extra_kwargs = {'password': {'write_only': True}}
    
    def save(self):
        executive = Executive(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            designation = self.validated_data['designation'],
            department = self.validated_data['department']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        executive.set_password(password)
        executive.save()
        return executive
 
class EmployeeRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            'email',
            'username',
            'role',
            'department',
            'password',
            'password2'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        employee = Employee(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            role = self.validated_data['role'],
            department = self.validated_data['department']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        employee.set_password(password)
        employee.save()
        return employee