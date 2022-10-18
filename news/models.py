from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    pic_src = models.CharField(
        max_length=255, 
        blank=True
    )
