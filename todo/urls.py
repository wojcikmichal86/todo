from django.urls import path
from .views import HelloAPI

urlpatterns = [
    path('api/hello/', HelloAPI.as_view()),
]
