from django import forms
from django.forms import ModelForm
from .models import Continent, Country, City

class ContinentForm(ModelForm):
    class Meta:
        model = Continent
        fields = ("name", "area", "population", "countries") 
        labels = {
            'name' : '',
            'area' : '',
            'population' : '',
            'countries' : '',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Continent name'}), 
            'area' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Continent area'}),
            'population' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Continent population'}),           
            'countries': forms.CheckboxSelectMultiple,
            
        }
                
class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ("name", "area", "population", "capital", "cities", "government")
        labels = {
            'name' : '',
            'area' : '',
            'population' : '',
            'capital' : 'Capital City',
            'government' : 'Form of Government',
            'cities' : 'Cities in the Country',
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Country name'}), 
            'area' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Country area'}),
            'population' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'Country population'}),           
            'capital' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Country capital'}),
            'government' : forms.Select(attrs={'class' : 'form-control', 'placeholder' : 'Country government'}),
            'cities' : forms.CheckboxSelectMultiple,
        }

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ("name", "area", "population", "is_capital")
        labels = {
            'name' : '',
            'area' : '',
            'population' : '',
            'is_capital' : 'Capital City',
        }
        
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'City name'}), 
            'area' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'City area'}),
            'population' : forms.NumberInput(attrs={'class' : 'form-control', 'placeholder' : 'City population'}),           
            'is_capital' : forms.CheckboxInput(attrs={'class' : 'form-control', 'placeholder' : 'Is capital city?'}),
        }
        
