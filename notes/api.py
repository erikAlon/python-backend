from rest_framework import serializers, viewsets
from .models import Notes, PersonalNotes


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = ('title', 'content')


class NotesViewset(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Notes.objects.all()


class PersonalNotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalNotes
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb
        # pdb.set_trace()
        user = self.context['request'].user
        personal_note = PersonalNotes.objects.create(
            user=user, **validated_data)
        return personal_note
        # pass


class PersonalNotesViewset(viewsets.ModelViewSet):
    serializer_class = PersonalNotesSerializer
    queryset = PersonalNotes.objects.all()
