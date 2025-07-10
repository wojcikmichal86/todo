from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Lista wszystkich zadań i tworzenie nowego zadania
class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Szczegóły jednego zadania, edycja i usuwanie
class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class HelloAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello from API"})