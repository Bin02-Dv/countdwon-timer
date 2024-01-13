from django.db import models

class Countdown(models.Model):
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f"{self.duration_minutes}"
