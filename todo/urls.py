from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    HelloAPI,
    TaskListCreateAPIView,
    TaskRetrieveUpdateDestroyAPIView,
    openapi_view,
    TaskDetailView
)

urlpatterns = [
    path('api/hello/', HelloAPI.as_view()),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-detail'),
    path("openapi.json", openapi_view),
    path("api/token-auth/", obtain_auth_token),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]