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
            b.cleanlinessTotal+=int(r["cleanliness"])
            b.cleanlinessNo+=1
        if r["hygiene"] != "":
            b.hygieneProductsTotal+=int(r["hygiene"])
            b.hygieneProductsNo+=1
        if r["accessibility"] != "":
            b.accessibilityTotal+=int(r["accessibility"])
            b.accessibilityNo+=1
        if r["safety"] != "":
            b.safetyTotal+=int(r["safety"])
            b.safetyNo+=1
        if r["periodProd"] != "":
            b.periodProducts=True
        b.save()
            
    return render(request, "mapRate/FrontEnd.html", {"bathrooms": Bathroom.objects.all()})