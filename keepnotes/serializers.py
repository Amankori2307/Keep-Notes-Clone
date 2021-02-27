from .models import Notes, Media, CheckBox
from rest_framework.serializers import ModelSerializer

class NotesListSerializer(ModelSerializer):
    class Meta:
        model = Notes
        exclude = ('createAt', 'updatedAt')