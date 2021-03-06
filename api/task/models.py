from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User,
        related_name='tasks',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
