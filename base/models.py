from django.db import models


class Startup (models.Model):
    name = models.CharField(max_length=255)
    members = models.TextField()
    fund = models.CharField(blank=True, null=True, max_length=1000)
    description = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=1255)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class StartupSubmit(models.Model):
    name = models.CharField(max_length=255)
    members_count = models.IntegerField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=255, blank=False, null=False)
    pitch = models.FileField(upload_to='base/pitches')

    def __str__(self):
        return self.name