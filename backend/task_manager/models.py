from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user
from simple_history.models import HistoricalRecords


class Task(models.Model):
    objects = models.Manager()

    STATUSES = [
        ('N', 'New'),
        ('P', 'Planned'),
        ('W', 'Work in progress'),
        ('C', 'Completed'),
    ]

    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUSES)
    planned_completion_date = models.DateField(blank=True, null=True)
    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            self.owner = user
        super().save(*args, **kwargs)

    def history_to_json(self):
        all_history = self.history.all()
        result = list()
        for episode in all_history:
            json = {
                'history_date': episode.history_date.strftime("%m-%d-%Y, %H:%M:%S"),
                'name': episode.name,
                'description': episode.description,
                'status': episode.status,
                'planned_completion_date': episode.planned_completion_date,
            }
            result.append(json)
        return {self.name: result}
