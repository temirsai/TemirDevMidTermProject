from django.db import models

class Task(models.Model):
    task = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title} to {self.deadline}'
