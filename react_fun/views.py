from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import PeopleList
from .serializers import PeopleListSerializer
from rest_framework import generics

class IndexView(TemplateView):
    template_name = 'index.html'

class PeopleListCreate(generics.ListCreateAPIView):
    queryset = PeopleList.objects.all()
    serializer_class = PeopleListSerializer