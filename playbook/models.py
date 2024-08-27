# models.py
from django.db import models

class Playbook(models.Model):
    play_name = models.CharField(max_length=255)
    roles = models.JSONField()
    blocks = models.JSONField()
    tasks = models.JSONField()
    version = models.CharField(max_length=50)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.play_name