from django.contrib import admin

# Register your models here.
from .models import Note
class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','content','created_at','updated_at']
admin.site.register(Note,NoteAdmin)