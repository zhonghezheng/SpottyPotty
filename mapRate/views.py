from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom, Permanent

# Create your views here.


def main(request):
    if len(Permanent.objects.all()) == 0:
        p = Permanent(cur_key = 0)
        p.save()

    if (request.method == "POST"):
        if request.POST["type"] == "add":
            r = request.POST
            p = Permanent.objects.all()[0]
            newBathroom = Bathroom(name=r["name"], longitude=r["lon"], latitude=r['lat'], rating=r["rating"], id = p.cur_key, peopleRated=1)
            p.cur_key = p.cur_key + 1
            p.save()
            newBathroom.save()
        elif request.POST["type"] == "rate":
            r = request.POST
            b = Bathroom.objects.get(id=r["id"])
            b.rating = (b.peopleRated * b.rating + int(r["rating"])) / (b.peopleRated+1)
            b.peopleRated += 1
            b.save()
    return render(request, "mapRate/main.html", {"bathrooms": Bathroom.objects.all()})