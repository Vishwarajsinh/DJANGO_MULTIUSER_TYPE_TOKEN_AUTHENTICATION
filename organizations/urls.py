from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'org', views.OrganizationViewSet)
router.register(r'org_loc', views.OrganizationLocationViewSet)
router.register(r'loc_brch', views.LocationBranchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
