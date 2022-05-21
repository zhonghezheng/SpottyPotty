from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom

# Create your views here.


def main(request):

    if (request.method == "POST"):
        if request.POST["type"] == "add":
            r = request.POST
           # newBathroom = Bathroom(name=r["name"], longitude=r["lon"], latitude=r['lat'], rating=r["rating"], peopleRated=1)

            newBathroom.save()
        elif request.POST["type"] == "rate":
            r = request.POST
           # b = Bathroom.objects.get(id=r["id"])
            #b.rating = (b.peopleRated * b.rating + int(r["rating"])) / (b.peopleRated+1)
            #b.peopleRated += 1
           # b.save()
    return render(request, "mapRate/main.html", {"bathrooms": Bathroom.objects.all()})