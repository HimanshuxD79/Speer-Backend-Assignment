from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Note
from users.models import CustomUser
from django.db.models import Q
# Create your views here.

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(Q(user=user) | Q(shared_with=user)).distinct()
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(Q(user=user) | Q(shared_with=user)).distinct()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def share_note(request, id):
    note = Note.objects.filter(id=id, user=request.user).first()
    if not note:
        return Response({"detail": "Note not found."}, status=404)
    if note.user != request.user:
        raise PermissionDenied("You don't have permission to share this note")
    
    emails_to_share_with = request.data.get('shared_with', [])
    valid_users = CustomUser.objects.filter(email__in=emails_to_share_with)
    valid_user_emails = [user.email for user in valid_users]
    invalid_user_emails = set(emails_to_share_with) - set(valid_user_emails)
    
    if invalid_user_emails:
        response_data = {
            "detail": "Some user emails were not added because they are invalid.",
            "valid_user_emails": valid_user_emails,
            "invalid_user_emails": list(invalid_user_emails),
        }
        return Response(response_data, status=400)
    
    for user in valid_users:
        note.shared_with.add(user)
    
    note.save()
    serializer = NoteSerializer(note)
    return Response(serializer.data)     

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def search_notes(request):
    query = request.query_params.get('q','')
    notes = Note.objects.filter(user=request.user,title__icontains=query)
    serializer = NoteSerializer(notes,many=True)
    return Response(serializer.data)