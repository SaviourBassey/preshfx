from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)