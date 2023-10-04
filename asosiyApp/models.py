from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    C = (
        ("Not started", "Not started"),
        ("In progress", "In progress"),
        ("Completed", "Completed"),
    )
    title = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=50, choices=C)
    detail = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def str(self):
        return self.title