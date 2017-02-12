from django import views
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from management.models.car import Car


def cars(request):
    cars = Car.objects.all().exclude(status='Broken')
    context = {}
    context['cars'] = cars
    return render(request, 'cars.html', context=context)
