from django.contrib import admin
from django.urls import path, include
from . import views
from .views import Logout
from rest_framework.authtoken.views import obtain_auth_token

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('exe_reg/', views.ExecutiveRegistration, name = "exe_reg"),
    path('emp_reg/', views.EmployeeRegistration, name = "emp_reg"),
    path('owner_reg/', views.OwnerRegistration, name = "owner_reg"),
    path('login/', obtain_auth_token, name = "login"),
    path('logout/', Logout.as_view(), name = "logout")

]
