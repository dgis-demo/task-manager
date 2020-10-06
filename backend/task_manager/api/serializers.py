from rest_framework import serializers
from task_manager.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'description', 'creation_time', 'status', 'planned_completion_date')
