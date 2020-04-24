from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=30, blank=True)
