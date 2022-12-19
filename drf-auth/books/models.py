from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=256)
    owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    desc=models.TextField(blank=True)

    def __str__(self):
        return self.name