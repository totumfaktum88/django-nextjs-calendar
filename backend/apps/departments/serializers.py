from rest_framework import serializers
from .models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department

        fields = ['id', 'name', 'description', 'manager_id']

        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField(required=True)
        description = serializers.CharField(required=False)