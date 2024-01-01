from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationCreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationListCreateView(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
