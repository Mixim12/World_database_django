from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    area = models.IntegerField()
    population = models.IntegerField()
    is_capital = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    area = models.IntegerField()
    population = models.IntegerField()
    capital = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='country', blank=True, null=True)
    cities = models.ManyToManyField(City, related_name='countries', blank=True)
    GOVERNMENT_CHOICES = [
        ('Democracy', 'Democracy'),
        ('Republic', 'Republic'),
        ('Monarchy', 'Monarchy'),
        ('Communism', 'Communism'),
        ('Dictatorship', 'Dictatorship'),
    ]
    government = models.CharField(max_length=100, choices=GOVERNMENT_CHOICES, default='democracy', blank=True, null=True)

    def __str__(self):
        return self.name

class Continent(models.Model):
    name = models.CharField(max_length=100)
    area = models.IntegerField()
    population = models.IntegerField()
    countries = models.ManyToManyField(Country, related_name='continents', blank=True)

    def __str__(self):
        return self.name


