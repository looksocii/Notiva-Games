from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

class Games(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    add_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Payment(models.Model):
    method = models.CharField(max_length=255)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    game = models.ForeignKey(to=Games, on_delete=models.CASCADE)

class Photos(models.Model):
    photo = models.ImageField(upload_to='images/')
    game = models.ForeignKey(to=Games, on_delete=models.CASCADE)

class Requirements(models.Model):
    os = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    graphics = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    game = models.ForeignKey(to=Games, on_delete=models.CASCADE)