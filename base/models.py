from django.db import models
from django.core.exceptions import ValidationError


class Startup (models.Model):
    name = models.CharField(max_length=255)
    members = models.IntegerField()
    fund = models.CharField(blank=True, null=True, max_length=1000)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='base/logos')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def positive_validator(value):
    if value <= 0:
        raise ValidationError("members count must be positive")


class StartupSubmit(models.Model):
    name = models.CharField(max_length=255)
    members_count = models.PositiveIntegerField(validators=[positive_validator])
    email = models.EmailField()
    phone = models.CharField(max_length=255, blank=True, null=True)
    pitch = models.FileField(upload_to='base/pitches')

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=False)
    image = models.ImageField(upload_to='base/events', blank=True, null=True)

    def __str__(self):
        return self.name


class Hire(models.Model):
    PUYESH = "PU"
    NORMAL = "NO"
    HIRE_TYPE = [
        (PUYESH, "Puyesh"),
        (NORMAL, "Normal"),
    ]
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    resume = models.FileField(upload_to='base/resumes')
    hireType = models.CharField(
        max_length=2,
        choices=HIRE_TYPE,
        default=NORMAL,
    )

    def __str__(self):
        return self.name
    # name - phone - email - file cv - type hire

class EventAttendees (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class WorkSpace (models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    