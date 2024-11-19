from django.db import models

class Department(models.Model):
    __tablename__ = "departments"

    name = models.CharField(max_length=255)
    description = models.TextField()

    manager = models.OneToOneField('employees.Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='managing_department')

    def __str__(self):
        return self.name