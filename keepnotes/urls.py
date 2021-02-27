from django.urls import path
from .views import NotesListView

urlpatterns = [
    path("list/", NotesListView.as_view(), name="get_or_create_notes")   
]