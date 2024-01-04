from django.db import models
from users.models import CustomUser

# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField( max_length=255)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    shared_with = models.ManyToManyField(CustomUser,related_name ='shared_notes',blank=True)