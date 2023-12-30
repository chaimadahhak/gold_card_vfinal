from django.db import models

# Create your models here.
# models.py
from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)
    cin = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} {self.surname} - CIN: {self.cin}'
