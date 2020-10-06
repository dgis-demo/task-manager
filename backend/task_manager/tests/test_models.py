from django.test import TestCase
from task_manager.models import Task


class TestTask(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            name='task',
            description='Simple task',
            status='N',
            planned_completion_date='2020-10-10'
        )

    def test_history_to_json(self):
        history = self.task.history_to_json()
        self.assertEqual(list(history.keys()), ['task'])
        self.assertEqual(history.get('task')[0].get('name'), 'task')
