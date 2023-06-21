from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPE = [
        ("A", "Admin"),
        ("K", "Korisnik"),
        ("F", "Firma"),
    ]
    tip = models.CharField(choices=USER_TYPE, default="K", max_length=1)