from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r'', EmployeeViewSet, basename='Employee')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),
]