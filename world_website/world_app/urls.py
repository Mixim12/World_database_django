from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('continents', views.continents, name='continents'),
    path('continents/add', views.add_continent, name='add_continent'),
    path('continents/update/<continent_id>', views.update_continent, name='update_continent'),
    path('continents/delete/<continent_id>', views.delete_continent, name='delete_continent'),
    
    path('countries', views.countries, name='countries'),
    path('countries/add', views.add_country, name='add_country'),
    path('countries/update/<country_id>', views.update_country, name='update_country'),
    path('countries/delete/<country_id>', views.delete_country, name='delete_country'),
    
    path('cities', views.cities, name='cities'),
    path('cities/add', views.add_city, name='add_city'),
    path('cities/update/<city_id>', views.update_city, name='update_city'),
    path('cities/delete/<city_id>', views.delete_city, name='delete_city'),
]
