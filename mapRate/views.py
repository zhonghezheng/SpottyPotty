from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom, Pin

# Create your views here.

def filter(pins, r):
    if r['m'] == "false" and r['f'] == "false" and r['i'] == "false":
        r['m'] = "true"
        r['f'] = "true"
        r['i'] = "true"
    filtered = []
    for pin in pins:
        candidates = []
        if r['m'] == "true" and pin.bathroom_male is not None:
            candidates.append(pin.bathroom_male)
        if r['f'] == "true" and pin.bathroom_female is not None:
            candidates.append(pin.bathroom_female)
        if r['i'] == "true" and pin.bathroom_inclusive is not None:
            candidates.append(pin.bathroom_inclusive)
        candidates = filter(lambda b: b.avg >= float(r["rating"]), candidates)
        candidates = filter(lambda b: r["paid"] == "false" or (r["paid"] == "true" and b.paidPeriodProducts), candidates)
        candidates = filter(lambda b: r["free"] == "false" or (r["free"] == "true" and b.freePeriodProducts), candidates)
        if len(candidates) > 0:
            filtered.append(pin)
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
            defaultPins = filter(defaultPins, r)
            
    return render(request, "mapRate/Frontend.html", {"pins": defaultPins})