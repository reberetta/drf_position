from django.shortcuts import render

from position.models import Position

from rest_framework import viewsets
from rest_framework import permissions
from position.serializers import PositionSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]