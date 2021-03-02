from django.urls import path
from .views import NotesListView, LabelListView

urlpatterns = [
    path("notes/", NotesListView.as_view(), name="get_or_create_notes"),
    path("label/", LabelListView.as_view(), name="get_or_create_label"),
]