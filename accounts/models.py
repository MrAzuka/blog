from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    STUDENT = 'STUD'
    EMPLOYED = 'EMPD'
    UNEMPLOYED = 'UEMP'
    OTHERS = 'OTHE'
    CAREER_CHOICES = [
        (STUDENT, 'STUD'),
        (EMPLOYED, 'EMPD'),
        (UNEMPLOYED, 'UEMP'),
        (OTHERS, 'OTHE')
    ]
    career_choices = models.CharField(
        max_length=4,
        choices=CAREER_CHOICES,
        default=STUDENT
    )
    age = models.PositiveIntegerField(null=True, blank=True)
