from django.urls import path
from .views import (
    HelloAPI,
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    openapi_view
)

urlpatterns = [
    path('api/hello/', HelloAPI.as_view()),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
path("openapi.json", openapi_view),
]