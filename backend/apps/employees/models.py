from django.db import models

class Employee(models.Model):
    __tablename__ = "employees"

    EMPLOYEE = 'employee'
    MANAGER = 'manager'

    POSITIONS = [
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=10, choices=POSITIONS, default=EMPLOYEE)

    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE, related_name='department_employees')

    def __str__(self):
        return self.name