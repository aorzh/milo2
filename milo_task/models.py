from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import random


class Profile(models.Model):
    user = models.OneToOneField(User)
    birthday = models.DateField()
    random_number = models.PositiveIntegerField(default=random.randint(1, 100),
                                                validators=[MinValueValidator(1), MaxValueValidator(100)])
