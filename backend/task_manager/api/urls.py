from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView)

urlpatterns = [
    path('', include(router.urls)),
    path('history/', views.get_history, name='get_history'),
    path('history/<int:task_id>/', views.get_task_history),
]
