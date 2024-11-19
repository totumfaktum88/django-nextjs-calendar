from rest_framework.test import APITestCase
from rest_framework import status
from apps.departments.models import Department

class DepartmentAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Human Resources")
        self.department_data = {"name": "Finance", "description": "Lorem ipsum"}

    def test_create_department_successful(self):
        response = self.client.post("/api/departments/", data=self.department_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], self.department_data["name"])

    def test_create_department_duplicate(self):
        duplicate_data = {"name": "Human Resources"}
        response = self.client.post("/api/departments/", data=duplicate_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_department_list(self):
        response = self.client.get("/api/departments/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.department.name)

    def test_update_department(self):
        update_data = self.department_data
        update_data["name"] = "Updated HR"

        response = self.client.put(f"/api/departments/{self.department.id}/", data=update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated HR")

    def test_delete_department(self):
        response = self.client.delete(f"/api/departments/{self.department.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Department.objects.filter(id=self.department.id).exists())
