from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom

# Create your views here.

def main(request):

    if (request.method == "POST"):
        b = Bathroom.objects.get(name="name")
        r = request.POST
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
            
    return render(request, "mapRate/FrontEnd.html", {"bathrooms": Bathroom.objects.all()})