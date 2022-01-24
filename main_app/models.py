from django.db import models

# Create your models here.

#model for what info a off road park has
class Offroad_Park(models.Model):
    name = models.CharField(max_length=75)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    image = models.CharField(max_length=9999)
    Difficulty = models.CharField(max_length=100, default="Easy")
    Duration = models.CharField(max_length=100, default="1 hour")
    Description = models.CharField(max_length=9999)
    open_verified = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

