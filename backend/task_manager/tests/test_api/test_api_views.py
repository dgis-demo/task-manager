import json
from rest_framework.test import APITestCase
from task_manager.models import Task


class TestTaskAPI(APITestCase):

    def setUp(self):
        self.api_prefix = '/api/task_manager/'
        self.client.post('/auth/users/', {"username": "user", "password": "!(@*!jijeidi1928)"})
        self.token = self.client.post('/auth/token/login/', {"username": "user", "password": "!(@*!jijeidi1928)"})\
            .data.get('auth_token')
        self.client.post(f'{self.api_prefix}tasks/', dict(
            name='task',
            description='Simple task',
            status='N',
            planned_completion_date='2020-10-10'
        ), HTTP_AUTHORIZATION=f'Token {self.token}')
        self.task = Task.objects.get(pk=1)

    def test_tasks_get(self):
        response = self.client.get(f'{self.api_prefix}tasks/', HTTP_AUTHORIZATION=f'Token {self.token}')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(content), 1)
        self.assertEqual(content[0].get('name'), 'task')

    def test_particular_task_get(self):
        response = self.client.get(f'{self.api_prefix}tasks/{self.task.id}/', HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(response.status_code, 200)

    def test_task_post(self):
        tasks = Task.objects.all()
        self.assertEqual(tasks.count(), 1)

    def test_task_del(self):
        del_response = self.client.delete(f'{self.api_prefix}tasks/{self.task.id}/',
                                          HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(del_response.status_code, 204)
        get_response = self.client.get(f'{self.api_prefix}tasks/{self.task.id}/',
                                       HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(get_response.status_code, 404)

    def test_task_put(self):
        put_response = self.client.put(f'{self.api_prefix}tasks/{self.task.id}/', data=dict(
            name='updated_task',
            description='Updated task',
            status='W',
            planned_completion_date='2020-10-20'
        ), HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(put_response.status_code, 200)
        get_response = self.client.get(f'{self.api_prefix}tasks/', HTTP_AUTHORIZATION=f'Token {self.token}')
        content = json.loads(get_response.content)
        self.assertEqual(len(content), 1)
        self.assertEqual('updated_task', content[0].get('name'))


class TestHistoryAPI(TestTaskAPI):

    def test_history(self):
        put_response = self.client.put(f'{self.api_prefix}tasks/{self.task.id}/', data=dict(
            name='updated_task',
            description='Updated task',
            status='W',
            planned_completion_date='2020-10-20'
        ), HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(put_response.status_code, 200)
        get_response = self.client.get(f'{self.api_prefix}history/', HTTP_AUTHORIZATION=f'Token {self.token}')
        content = json.loads(get_response.content)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(list(content.get('history')[0].keys()), ['updated_task'])
        self.assertEqual(len(content.get('history')[0].get('updated_task')), 2)

    def test_particular_task_history(self):
        post_response = self.client.post(f'{self.api_prefix}tasks/', dict(
            name='task2',
            description='New task',
            status='W',
            planned_completion_date='2020-10-20'
        ), HTTP_AUTHORIZATION=f'Token {self.token}')
        self.assertEqual(post_response.status_code, 201)
        get_response = self.client.get(f'{self.api_prefix}history/{self.task.id}/', HTTP_AUTHORIZATION=f'Token {self.token}')
        content = json.loads(get_response.content)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(list(content.get('task_history').keys()), ['task'])
        self.assertEqual(len(content.get('task_history').get('task')), 1)
