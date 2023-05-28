from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Car,Osoba

def index(response):
    cars = Car.objects.all()
    return render(response, 'search/home.html', {'cars': cars})

def carsearch(request):
    make = request.GET.get('make')
    model = request.GET.get('model')
    year = request.GET.get('year')

    cars = Car.objects.all()

    if make:
        cars = cars.filter(make__icontains=make)
    if model:
        cars = cars.filter(model__icontains=model)
    if year:
        cars = cars.filter(year=year)

    return render(request, 'search/carsearch.html', {'cars': cars})

def carcreate(request):
    if request.method == 'POST':
        make = request.POST.get('make')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        description = request.POST.get('description')

        Car.objects.create(make=make, model=model, year=year, price=price, description=description)
        return redirect('index')

    return render(request, 'search/carcreate.html')