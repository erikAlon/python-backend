from django.contrib import admin

# Register your models here.
from .models import Notes
from .models import PersonalNotes

admin.site.register(Notes)
admin.site.register(PersonalNotes)
