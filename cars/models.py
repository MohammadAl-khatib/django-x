from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.urls import reverse

class car (models.Model):
    name = models.CharField(max_length=15)
    price = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('car_detail', args = [self.id]) 
