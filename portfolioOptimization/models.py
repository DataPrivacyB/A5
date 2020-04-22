from django.db import models
from django.contrib.auth.models import User

class SharesType(models.Model):
    Name = models.CharField(max_length=100)
    Type = models.IntegerField()

    def __str__(self):
        return self.Name

class Portfolio(models.Model):
    Share = models.CharField(max_length=100)

    def __str__(self):
        return self.Share
