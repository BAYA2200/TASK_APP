from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView

from CRM.models import Task, Clients
from CRM.serializers import TaskSerializer, SearchSerializer, ClientsSerializer
from .filters import ProductFilter


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializers_class = TaskSerializer


class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializers_class = TaskSerializer


class SearchTaskAPIView(APIView):
    queryset = Task.objects.all()
    serializers_class = SearchSerializer
    filter_backend = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ClientsList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class ClientsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer

