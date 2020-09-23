from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'org', views.OrganizationViewSet)
router.register(r'org_loc', views.OrganizationLocationViewSet)
router.register(r'loc_brch', views.LocationBranchViewSet)
# router.register(r'users', views.UsersViewSet)
# router.register(r'employee', views.EmployeeViewSet)
# router.register(r'customer', views.CustomerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
