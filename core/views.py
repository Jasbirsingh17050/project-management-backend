from rest_framework import viewsets
from .models import User, Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("id")
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by("id")
    serializer_class = ProjectSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("project", "assigned_to").all().order_by("id")
    serializer_class = TaskSerializer