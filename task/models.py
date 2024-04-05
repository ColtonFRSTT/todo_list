from django.db import models

# Create your models here.

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100, null = False, blank = False)
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_name

