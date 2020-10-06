from django.test import TestCase
from django.urls import reverse, resolve
from task_manager.api import views


class TestApiUrls(TestCase):

    def test_get_history(self):
        url = reverse('get_history')
        self.assertEqual(resolve(url).func, views.get_history)
