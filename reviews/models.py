from django.db import models

# Create your models here.

class Review(models.Model):
    user = models.CharField(max_length=20)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user} {self.review} {self.rating}"
