from django.db import models

# Create your models here.
class todo_task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title