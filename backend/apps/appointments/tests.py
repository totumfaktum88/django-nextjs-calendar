from datetime import datetime
from rest_framework.test import APITestCase
from rest_framework import status
from apps.appointments.models import Appointment
from apps.employees.models import Employee
from apps.departments.models import Department

class AppointmentAPITests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT")
        self.employee = Employee.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            position="employee",
            department=self.department,
        )
        self.appointment_data = {
            "title": "Team Meeting",
            "description": "Lorem ipsum",
            "start_date": "2024-11-15 10:00:00",
            "end_date": "2024-11-15 10:00:00",
            "employee": self.employee.id,
        }

        self.appointment = Appointment.objects.create(
            title="Project Discussion",
            description="Lorem ipsum",
            start_date="2024-11-15 10:00:00",
            end_date="2024-11-15 10:00:00",
            employee=self.employee,
        )

    def test_create_appointment_successful(self):
        response = self.client.post("/api/appointments/", data=self.appointment_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], self.appointment_data["title"])
        self.assertEqual(response.data["start_date"],
            datetime.strptime(
                self.appointment_data["start_date"],
                "%Y-%m-%d %H:%M:%S"
            ).isoformat() + "Z"
        )
        self.assertEqual(
            response.data["end_date"],
            datetime.strptime(
                self.appointment_data["end_date"],
                "%Y-%m-%d %H:%M:%S"
            ).isoformat() + "Z"
        )
        self.assertEqual(response.data["description"], self.appointment_data["description"])
        self.assertEqual(response.data["employee"], self.employee.id)

    def test_create_appointment_invalid_date(self):
        invalid_data = self.appointment_data.copy()
        invalid_data["start_date"] = "invalid-date"
        invalid_data["end_date"] = "invalid-date"
        response = self.client.post("/api/appointments/", data=invalid_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_appointment_list(self):
        response = self.client.get("/api/appointments/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.appointment.title)

    def test_update_appointment(self):
        update_data = self.appointment_data
        update_data["title"] = "Updated Meeting"
        response = self.client.put(f"/api/appointments/{self.appointment.id}/", data=update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Meeting")

    def test_delete_appointment(self):
        response = self.client.delete(f"/api/appointments/{self.appointment.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Appointment.objects.filter(id=self.appointment.id).exists())
