from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContinentForm, CountryForm, CityForm
from .models import Continent, Country, City
from django.http import HttpResponseRedirect
from .models import Continent, Country, City

def index(request):
    return render(request, 'world_app/index.html')

def continents(request):
    continents = Continent.objects.all()
    return render(request, 'world_app/continents.html',{'continents' : continents})

def add_continent(request):
    submitted = False
    if request.method == "POST":
        form = ContinentForm(request.POST)
        if form.is_valid():
            continent = form.save(commit=False)
            continent.save()
            return HttpResponseRedirect('add?submitted=True')	
    else:
        form = ContinentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'world_app/add_continent.html',{'form' : form, 'submitted' : submitted})

def update_continent(request, continent_id):
    continent = Continent.objects.get(pk=continent_id)
    form = ContinentForm(request.POST or None, instance=continent)
    if form.is_valid():
        form.save()
        return redirect('/continents')
    
    return render(request, 'world_app/update_continent.html',{'continent' : continent, 'form' : form})

def delete_continent(request, continent_id):
    continent = get_object_or_404(Continent, id=continent_id)

    if request.method == 'POST':
        form = ContinentForm(request.POST, instance=continent)
        continent.delete()
        return redirect('/continents')  
    else:   
        form = ContinentForm(instance=continent)

    return render(request, 'world_app/delete_continent.html', {'continent': continent, 'form': form})

def countries(request):
    countries = Country.objects.all()
    return render(request, 'world_app/countries.html',{'countries' : countries})

def add_country(request):
    submitted = False
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            country = form.save(commit=False)
            country.save()
            return 	HttpResponseRedirect('add?submitted=True')	
    else:
        form = CountryForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'world_app/add_country.html',{'form' : form, 'submitted' : submitted})

def update_country(request, country_id):
    country = Country.objects.get(pk=country_id)
    form = CountryForm(request.POST or None, instance=country)
    if form.is_valid():
        form.save()
        return redirect('/countries')
    
    return render(request, 'world_app/update_country.html',{'country' : country, 'form' : form})

def delete_country(request, country_id):
    country = get_object_or_404(Country, id=country_id)

    if request.method == 'POST':
        form = CountryForm(request.POST, instance=country)
        country.delete()
        return redirect('/countries')  
    else:   
        form = CountryForm(instance=country)

    return render(request, 'world_app/delete_country.html', {'country': country, 'form': form})

def cities(request):
    cities = City.objects.all()
    return render(request, 'world_app/cities.html',{'cities' : cities})


def add_city(request):
    submitted = False
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.save(commit=False)
            city.save()
            return 	HttpResponseRedirect('add?submitted=True')	
    else:
        form = CityForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'world_app/add_city.html',{'form' : form, 'submitted' : submitted})

def update_city(request, city_id):
    city = City.objects.get(pk=city_id)
    form = CityForm(request.POST or None, instance=city)
    if form.is_valid():
        form.save()
        return redirect('/cities')
    
    return render(request, 'world_app/update_city.html',{'city' : city, 'form' : form})

def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)

    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        city.delete()
        return redirect('/cities')  
    else:   
        form = CityForm(instance=city)

    return render(request, 'world_app/delete_city.html', {'city': city, 'form': form})