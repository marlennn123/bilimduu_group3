from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class CarView(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['price', 'marka', 'title']
    search_fields = ['title']
    pagination_class = StandardResultsSetPagination


class CarBetView(ModelViewSet):
    queryset = CarBet.objects.all()
    serializer_class = CarBetSerializer