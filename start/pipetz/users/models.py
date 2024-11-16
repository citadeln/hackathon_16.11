from django.contrib.auth.models import AbstractUser
from django.db import models
from competitions.models import Competitions

class User(AbstractUser):
    pass

class StudentToTeacher(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student', primary_key=True)
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher')
    competition_id = models.ForeignKey(Competitions, on_delete=models.CASCADE, related_name='competition')
    password = models.CharField(max_length=255)