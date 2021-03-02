from .models import Notes, Media, CheckBox, Label
from rest_framework.serializers import ModelSerializer


class LabelSerializer(ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class NotesSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

class NotesListSerializer(ModelSerializer):
    class Meta:
        model = Notes
        exclude = ('createdAt', 'updatedAt')

