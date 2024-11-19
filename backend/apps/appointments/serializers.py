from rest_framework import serializers
from .models import Appointment
from apps.employees.models import Employee

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

        title = serializers.CharField(required=True)
        description = serializers.EmailField(required=True)
        start_date = serializers.DateTimeField(required=True)
        end_date = serializers.DateTimeField(required=True)

        employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())