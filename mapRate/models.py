from django.db import models

# Create your models here.
class Bathroom(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    rating = models.FloatField()
    peopleRated = models.IntegerField()

    def __str__(self):
        return f"{self.name}: ({self.latitude}, {self.longitude}), {self.rating}*"

class Permanent(models.Model):
    cur_key = models.IntegerField()