from rest_framework.response import Response
from rest_framework import status, views
from rest_framework.authentication import TokenAuthentication
from utils.customPermissions import NotesPermission, LabelPermission
from utils.helperFunctions import getNotesForUser, genResponse
from .models import Notes, CheckBox, Media
from .serializers import NotesListSerializer, NotesSerializer, LabelSerializer
# Create your views here.

class NotesListView(views.APIView):
    permission_classes = [NotesPermission]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data
        data["userRef"] = request.user.id
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                genResponse(False, True, "Created Notes Successfully", serializer.data)
            )
        else:
            return Response(
                genResponse(True, False, serializer.errors)
            )
        
    def get(self, request):
        notes = getNotesForUser(Notes, request.user.id)
        serializedNotes = NotesListSerializer(notes, many=True)

        return Response(
            genResponse(False, True, "List Of Notes", serializedNotes.data)
        )
        

class LabelListView(views.APIView):
    permission_classes = [LabelPermission]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        data = request.data
        data["userRef"] = request.user.id
        serializer = LabelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                genResponse(False, True, "Label Created Successfully", serializer.data)
            )
        else:
            return Response(
                genResponse(True, False, serializer.errors)
            )