from rest_framework import serializers
from .models import Employee
from apps.departments.models import Department


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

        name = serializers.CharField(required=True)
        email = serializers.EmailField(required=True)
        position = serializers.ChoiceField(required=True, choices=Employee.POSITIONS)
        department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())