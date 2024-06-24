from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    @action(methods=['get'], detail=True)
    def persons_in_team(self, request, pk):
        persons = Person.objects.filter(team_id=pk)
        team = Team.objects.get(id=pk)
        return Response({f'persons in team {team.name}': PersonSerializer(persons, many=True).data})
