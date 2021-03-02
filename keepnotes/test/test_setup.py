from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import MyUser, Notes, Label
from rest_framework.authtoken.models import Token

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


class TestSetupForViews(APITestCase):
    def setUp(self):
        
        # Urls
        self.notes_list_url = reverse("get_or_create_notes")
        self.register_url = "/auth/users/"
        self.login_url = "/auth/token/login"

        # Data
        self.user_data = {
            "username": "test",
            "email": "test@gmail.com",
            "password": "test"
        }

        self.user = MyUser.objects.create(username="test1", password="password", email="test1@gmail.com")
        self.users = MyUser.objects.all()
        self.login_data = {
            "email": "test@gmail.com",
            "password": "test"
        }
        self.label = Label.objects.create(userRef=self.user, name="Label1")
        self.note_data = {
            "title": "Title",
            "text": "Text is here",
            "userRef": self.user.id,
            "labelRef": self.label.id
        }
        self.auth_token =  Token.objects.create(user=self.user)
        

    def tearDown(self):
        return super().tearDown()
