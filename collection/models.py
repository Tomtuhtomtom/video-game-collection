from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Collection(models.Model):
    name = models.CharField(max_length=100, help_text='Enter name of collection')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='collections')

    def __str__(self):
        return f"{self.owner}'s {self.name}"