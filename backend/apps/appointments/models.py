from django.db import models

class Appointment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    employee = models.ForeignKey('employees.Employee', on_delete=models.CASCADE, related_name='appointments')

    def __str__(self):
        return f"{self.title} - {self.employee.name} - {self.start_date} - {self.end_date}"
