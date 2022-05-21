from django.db import models

# Create your models here.
class Bathroom(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    genders = models.CharField(max_length=1)
    cleanlinessTotal = models.FloatField()
    cleanlinessNo = models.IntegerField(default=0)
    hygieneProductsTotal = models.FloatField()
    hygieneProductsNo = models.IntegerField(default=0)
    periodProducts = models.BooleanField()
    accessibilityTotal = models.FloatField()
    accessibilityNo = models.IntegerField(default=0)
    safetyTotal = models.FloatField()
    safetyNo = models.IntegerField(default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.name}: ({self.latitude}, {self.longitude})*"

    def cAvg(self):
        return self.cleanlinessTotal/self.cleanlinessNo
    def hAvg(self):
        return self.hygieneProductsTotal/hygieneProductsNo
    def aAvg(self):
        return self.accessibilityTotal/accessibilityNo
    def sAvg(self):
        return safetyTotal/safetyNo
