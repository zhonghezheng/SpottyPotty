from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom, Pin

# Create your views here.

def filter(pins, r):
    filtered = []
    # do stuff
    return filtered

def main(request):
    defaultPins = Pin.objects.all()
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
            
            pins = Pin.objects.all()
            filtered = []
            
            for pin in pins:
                if r["m"] == "true" and pin.bathroom_male is None:
                    continue
                if r["f"] == "true" and pin.bathroom_female is None:
                    continue
                if r["i"] == "true" and pin.bathroom_inclusive is None:
                    continue
                bathrooms = [pin.bathroom_male, pin.bathroom_female, pin.bathroom_inclusive]
                for bathroom in bathrooms:
                    if bathroom is None:
                        continue
                    if r["free"] == "true" and bathroom.


                if r["free"] == "true" and pin
                filtered.append(pin)

            
            # <QueryDict: {'csrfmiddlewaretoken': ['IioMdDhDrWy7Y5I04LMcVpuF89CxHiVjKi6qC7hbtyXtMiYhJ2Jrnj7dTLcp50Zw'], 'type': ['filter'], 'm': ['false'], 'w': ['false'], 'i': ['false'], 'free': ['false'], 'paid': ['false'], 'distance': ['5'], 'rating': ['5']}>

            defaultPins = filtered
            print(r)
            
    return render(request, "mapRate/Frontend.html", {"pins": defaultPins})