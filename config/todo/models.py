from pydoc import describe
from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField("やること", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締め切り")

    def __str__(self):
        return self.title
