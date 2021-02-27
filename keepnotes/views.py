from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.authentication import TokenAuthentication
from utils.customPermissions import NotesPermission
from utils.helperFunctions import getNotesForUser, genResponse
from .models import Notes, CheckBox, Media
from .serializers import NotesListSerializer
# Create your views here.

class NotesListView(views.APIView):
    permission_classes = [NotesPermission]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        notes = getNotesForUser(Notes, request.user.id)
        serializedNotes = NotesListSerializer(notes, many=True)

        return Response(
            genResponse(False, True, "List Of Notes", serializedNotes.data)
        )
        