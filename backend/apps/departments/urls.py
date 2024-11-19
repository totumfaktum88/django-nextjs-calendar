from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet

router = DefaultRouter()
router.register(r'', DepartmentViewSet, basename='Department')

urlpatterns = [
    path('', include(router.urls)),
]