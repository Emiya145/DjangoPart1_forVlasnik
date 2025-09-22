from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    year = models.IntegerField()

    def __str__(self):
        return self.title
