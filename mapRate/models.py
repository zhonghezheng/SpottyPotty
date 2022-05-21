from django.db import models

# Create your models here.
class Bathroom(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    genders = models.CharField(max_length=1)
    cleanliness = models.FloatField()
    cleanlinessNo = models.IntegerField(default=0)
    hygeine_products = models.FloatField()
    hygeine_productsNo = models.IntegerField(default=0)
    accessibility = models.FloatField()
    accessibilityNo = models.IntegerField(default=0)
    safety = models.FloatField()
    safetyNo = models.IntegerField(default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return f"{self.name}: ({self.latitude}, {self.longitude}), {self.rating}*"
