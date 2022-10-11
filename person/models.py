from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name  = models.CharField(max_length= 250, blank=False, default="")
    last_name  = models.CharField(max_length= 250, blank=False, default="")
