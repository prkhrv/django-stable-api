from django.shortcuts import render
from .serializers import StudentSerializer
from client.models import Student
from rest_framework import viewsets

# Create your views here.

class StudentApiView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    http_method_names = ['get']
