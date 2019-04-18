from django.db import models
from django.contrib.auth.models import User

from .user_constants import UserConstant


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=UserConstant.GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(null=True)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, default=3)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=255, null=True)
    academic_year = models.IntegerField(
        choices=UserConstant.YEAR_CHOICES, null=True)
    marks = models.FloatField(null=True)
    caste = models.CharField(
        max_length=200, choices=UserConstant.CASTE_CHOICES, null=True)


class Organisation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
