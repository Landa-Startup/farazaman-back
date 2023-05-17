from django.db import models


class Startup (models.Model):
    name = models.CharField(max_length=255)
    members = models.TextField()
    fund = models.CharField(blank=True, null=True, max_length=1000)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=1255)

    def __str__(self):
        return self.name
    