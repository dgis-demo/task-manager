from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TaskSerializer
from task_manager.models import Task


class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'planned_completion_date']
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


@api_view(['GET'])
def get_history(request):
    queryset = Task.objects.filter(owner=request.user)
    result = [task.history_to_json() for task in queryset]
    return JsonResponse({'history': result})


@api_view(['GET'])
def get_task_history(request, task_id):
    task = get_object_or_404(Task, owner=request.user, pk=task_id)
    return JsonResponse({'task_history': task.history_to_json()})
