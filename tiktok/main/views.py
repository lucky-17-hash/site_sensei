from django.shortcuts import render

from .models import Car

def index(request):
    all_cars = Car.objects.all()
    return render(request, "index.html", {"Cars":all_cars})
