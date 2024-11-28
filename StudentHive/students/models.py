# students/models.py

from django.db import models
from django.utils import timezone  # Import timezone

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)  # Use only default

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
