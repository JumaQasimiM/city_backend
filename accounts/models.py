from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_ROLE = [
        ('admin', 'Admin'),
        ('business', 'Business Owner'),
        ('user', 'User'),
        ('viewer', 'Viewer'),
    ]

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    role = models.CharField(
        max_length=20,
        choices=USER_ROLE,
        default='user'
    )

    bio = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.first_name