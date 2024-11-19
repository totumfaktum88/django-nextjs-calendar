from rest_framework.test import APITestCase
from rest_framework import status
from apps.departments.models import Department
from apps.employees.models import Employee

class EmployeeAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="HR")
        self.employee_data = data ={
            "name": "John Doe",
            "email": "john.doe@example.com",
            "position": "employee",
            "department": self.department.id,
        }

        self.employee = Employee.objects.create(
            name="Jane Smith",
            email="jane.smith@example.com",
            position="manager",
            department=self.department,
        )

    def test_create_employee_successful(self):
        response = self.client.post("/api/employees/", data=self.employee_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], self.employee_data["name"])
        self.assertEqual(response.data["email"], self.employee_data["email"])
        self.assertEqual(response.data["position"], self.employee_data["position"])
        self.assertEqual(response.data["department"], self.department.id)

    def test_create_employee_invalid_department(self):
        invalid_data = self.employee_data.copy()
        invalid_data["department"] = 999
        response = self.client.post("/api/employees/", data=invalid_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("department", response.data)

    def test_get_employee_list(self):
        response = self.client.get("/api/employees/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.employee.name)
        self.assertEqual(response.data[0]["email"], self.employee.email)

    def test_filter_employee_by_email(self):
        response = self.client.get("/api/employees/?search=jane")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Jane Smith")
        self.assertEqual(response.data[0]["email"], "jane.smith@example.com")

        response = self.client.get("/api/employees/?search=jane.smith@example")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Jane Smith")
        self.assertEqual(response.data[0]["email"], "jane.smith@example.com")

    def test_update_employee(self):
        update_data = self.employee_data
        update_data["name"] = "John Updated"
        response = self.client.put(f"/api/employees/{self.employee.id}/", data=update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "John Updated")

    def test_delete_employee(self):
        response = self.client.delete(f"/api/employees/{self.employee.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Employee.objects.filter(id=self.employee.id).exists())
