from django.db import models
from profiles.models import Profile
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class Skill(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    score = models.PositiveIntegerField()

    def __str__(self):
        return "{}--{}--{}".format(self.user, self.name, self.score)