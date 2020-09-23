from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import decorators, permissions, status
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

User = get_user_model()

# Create your views here.

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def OwnerRegistration(request):
    serializer = OwnerRegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        owner = serializer.save()
        data['response'] = "success"
        data['email'] = owner.email
        data['username'] = owner.username
        data['company_name'] = owner.company_name
        data['GST'] = owner.GST
        data['PAN'] = owner.PAN
        token = Token.objects.get(user=owner).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def ExecutiveRegistration(request):
    serializer = ExecutiveRegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        executive = serializer.save()
        data['response'] = "success"
        data['email'] = executive.email
        data['username'] = executive.username
        data['designation'] = executive.designation
        data['department'] = executive.department
        token = Token.objects.get(user=executive).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)

@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def EmployeeRegistration(request):
    serializer = EmployeeRegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        employee = serializer.save()
        data['response'] = "success"
        data['email'] = employee.email
        data['username'] = employee.username
        data['role'] = employee.role
        data['department'] = employee.department
        token = Token.objects.get(user=employee).key
        data['token'] = token
    else:
        data = serializer.errors
    return Response(data)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
