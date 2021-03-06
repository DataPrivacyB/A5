from django.db import models
from django.contrib.auth.models import User

photo = models.ImageField(upload_to="images")

class Shares(models.Model):
    Name = models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class EncShares(models.Model):
    Name = models.CharField(max_length=1000)
    def __str__(self):
        return self.Name



class SharesHeld(models.Model):
    Name = models.CharField(max_length=1000)
    Price = models.FloatField()
    Quantity = models.BigIntegerField()
    #owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')


    def __str__(self):
        return f'{self.user.username} Profile'
