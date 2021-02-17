from django.db import models

class Car(models.Model):
    color = models.CharField(max_length=255)
    wheels = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return f"Car with {self.color} color {self.wheels} wheels"