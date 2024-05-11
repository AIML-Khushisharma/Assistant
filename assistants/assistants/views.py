from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import filters
from .models import Assistant
from .serializers import AssistantSerializer


class AssistantListAPIView(ListCreateAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'department', 'role']
    ordering_fields = ['name', 'department', 'role']


class AssistantDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer
