from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import MyUser, Notes

class TestSetupForModel(APITestCase):
    def setUp(self):
        
        self.user_data = {
            "username": "test",
            "email": "test@gmail.com",
            "password": "test"
        }
        self.user = MyUser.objects.create(username="test1", password="test1", email="test1@gmail.com")

        self.labelName = "My Label"

        # Media Data
        self.note = Notes.objects.create(userRef=self.user)
        self.value = "http://localhost:8000/admin/keepnotes/myuser/"

        # checkbox Data
        self.text = "Workout"
        self.status = True

        # Collaberator Data
        self.note = Notes.objects.create(userRef=self.user)
        self.collaberator = MyUser.objects.create(username="test2", password="test2", email="test2@gmail.com")


    def tearDown(self):
        return super().tearDown()
