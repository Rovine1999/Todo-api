from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title