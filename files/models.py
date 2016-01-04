from django.db import models

# Create your models here.

class File(models.Model):
    name = models.CharField(max_length = 255)
    path = models.CharField(max_length = 255)
    date = models.DateField(auto_now = True)
