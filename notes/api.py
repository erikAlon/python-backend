from rest_framework import serializers, viewsets
from .models import Notes


class NotesSerializer(serializers.HyperlinnkedModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'content')


class NotesViewset(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()
