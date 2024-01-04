from django.urls import path
from .views import NoteListCreateView,NoteDetailView,share_note,search_notes

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('notes/<int:id>/share/', share_note, name='share-note'),
    path('notes/search/', search_notes, name='search-notes'),
]