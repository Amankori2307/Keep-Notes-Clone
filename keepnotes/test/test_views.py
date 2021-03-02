from .test_setup import TestSetupForViews
from rest_framework import status
import pdb


class NotesViewsTestCase(TestSetupForViews):
    def test_check_if_user_can_register(self):
        res = self.client.post(self.register_url, data=self.user_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_if_user_can_get_auth_token(self):
        # Register
        self.client.post(self.register_url, data=self.user_data, format="json")
        # Authenticate
        res = self.client.post(self.login_url, data=self.login_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_check_unauthorized_request_should_not_get_data(self):
        res = self.client.get(self.notes_list_url, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_check_if_authorized_user_can_get_notes_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.auth_token.key)
        res = self.client.get(self.notes_list_url, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_check_if_user_can_create_note_with_no_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.auth_token.key)
        res = self.client.post(self.notes_list_url, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
    def test_check_if_user_can_create_note_with__data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.auth_token.key)
        res = self.client.post(self.notes_list_url, data=self.note_data ,format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    
    def test_if_unauthorized_user_cannot_create_note(self):
        res = self.client.post(self.notes_list_url, data=self.note_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
