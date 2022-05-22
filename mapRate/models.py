from django.db import models

class Rating(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    total = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    average = models.FloatField(default=0.0)
    
    def update_avg(self):
        if self.count == 0:
            self.average = 0
        else:
            self.average = self.total / self.count
            self.average = round(self.average, 1)
        self.save()

    def __str__(self):
        return str(self.average)

# Create your models here.
class Bathroom(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1) 
    freePeriodProducts = models.BooleanField()
    paidPeriodProducts = models.BooleanField()

    cleanliness = models.ForeignKey(Rating, on_delete=models.PROTECT, related_name="c")
    hygiene = models.ForeignKey(Rating, on_delete=models.PROTECT, related_name="h")
    safety = models.ForeignKey(Rating, on_delete=models.PROTECT, related_name="s")
    accessiblity = models.ForeignKey(Rating, on_delete=models.PROTECT, related_name="a")
    avg = models.FloatField(default=0)

    def update(self):
        self.cleanliness.update_avg()
        self.hygiene.update_avg()
        self.safety.update_avg()
        self.accessiblity.update_avg()
        self.avg = round((self.cleanliness.average+self.hygiene.average+self.safety.average+self.accessiblity.average)/4, 1)
 

    def __str__(self):
        ret =  str(self.gender)+","+str(self.freePeriodProducts)+","+str(self.paidPeriodProducts)+","
        ret += str(self.cleanliness)+","+str(self.hygiene)+","+str(self.safety)+","+str(self.accessiblity)+","+str(self.avg)
        return ret

class Pin(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    bathroom_male = models.ForeignKey(Bathroom, on_delete=models.CASCADE, related_name="m", blank=True, null=True)
    bathroom_female = models.ForeignKey(Bathroom, on_delete=models.CASCADE, related_name="f", blank=True, null=True)
    bathroom_inclusive = models.ForeignKey(Bathroom, on_delete=models.CASCADE, related_name="i", blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()   
    

    def __str__(self):
        return f"male: {str(self.bathroom_male)},\
                 female:{str(self.bathroom_female)},\
                 inclusive:{str(self.bathroom_inclusive)}"
