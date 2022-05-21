from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import Bathroom, Pin

# Create your views here.

def products_filter(bathroom, free, paid):
    if not free and not paid:
        return True
    if not free and paid:
        return bathroom.paidPeriodProducts
    if free and not paid:
        return bathroom.freePeriodProducts
    if free and paid:
        return bathroom.paidPeriodProducts or bathroom.freePeriodProducts

def filter_dict(pins, r):
    for k in r:
        r[k] = r[k][0]
    if r["m"] == 'false' and r["f"] == 'false' and r["i"] == 'false':
        r["m"] = "true"
        r["f"] = "true"
        r["i"] = "true"
    filtered = []
    for pin in pins:
        candidates = []
        if r["m"] == "true" and pin.bathroom_male is not None:
            candidates.append(pin.bathroom_male)
        if r["f"] == "true" and pin.bathroom_female is not None:
            candidates.append(pin.bathroom_female)
        if r["i"] == "true" and pin.bathroom_inclusive is not None:
            candidates.append(pin.bathroom_inclusive)
        candidates = list(filter(lambda b: b.avg >= float(r["rating"]), candidates))
        candidates = list(filter(lambda b: products_filter(b, r["free"] == "true", r["paid"] == "true"), candidates))
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
            defaultPins = filter_dict(defaultPins, dict(r))
            
    return render(request, "mapRate/Frontend.html", {"pins": defaultPins})
