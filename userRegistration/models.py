from django.db import models
# Create your models here.

class Users(models.Model):
  id = models.AutoField
  username = models.CharField(max_length=255)
  password = models.CharField(max_length=255)