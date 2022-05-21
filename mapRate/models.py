from django.db import models

class Rating():
    total = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    
    def update_avg(self):
        if self.count == 0:
            self.average = 0
        else:
            self.average = self.total / self.count

    def __str__(self):
        return str(self.average)

# Create your models here.
class Bathroom(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    genders = models.CharField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()    
    periodProducts = models.BooleanField()

    cleanliness = models.ForeignKey(Rating, on_delete=models.PROTECT)
    hygiene = models.ForeignKey(Rating, on_delete=models.PROTECT)
    safety = models.ForeignKey(Rating, on_delete=models.PROTECT)
    accessiblity = models.ForeignKey(Rating, on_delete=models.PROTECT)

    def update(self):
        self.cleanliness.update_avg()
        self.hygiene.update_avg()
        self.safety.update_avg()
        self.accessiblity.update_avg()
    
    # cleanlinessTotal = models.FloatField()
    # cleanlinessNo = models.IntegerField(default=0)
    # hygieneProductsTotal = models.FloatField()
    # hygieneProductsNo = models.IntegerField(default=0)
    # accessibilityTotal = models.FloatField()
    # accessibilityNo = models.IntegerField(default=0)
    # safetyTotal = models.FloatField()
    # safetyNo = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.name}: ({self.latitude}, {self.longitude})*"

# class Pin(models.Model):
#     bathroom_male = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
#     bathroom_female = models.ForeignKey(Bathroom, on_delete=models.CASCADE)
#     bathroom_inclusive = models.ForeignKey(Bathroom, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"male: {str(self.bathroom_male)} \n\
#                  female:{str(self.bathroom_female)}\n\
#                  inclusive:{str(self.bathroom_inclusive)}\n"