from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom, Pin

# Create your views here.

def main(request):

    if (request.method == "POST"):
        r = request.POST
        if r["type"] == "rate":
            b = Bathroom.objects.get(name="name")
            if r["cleanliness"] != "":
                b.cleanliness.total += int(r["cleanliness"])
                b.cleanliness.count += 1
            if r["hygiene"] != "":
                b.hygiene.total += int(r["cleanliness"])
                b.hygiene.count += 1
            if r["accessibility"] != "":
                b.accessibility.total += int(r["cleanliness"])
                b.accessibility.count += 1
            if r["safety"] != "":
                b.safety.total += int(r["cleanliness"])
                b.safety.count += 1
            if r["periodProd"] != "":
                b.periodProducts=True
            b.save()
        elif r["type"] == "filter":
            print(r)
            
    return render(request, "mapRate/Frontend.html", {"pins": Pin.objects.all()})