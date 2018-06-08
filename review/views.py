from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Avg
from .models import Restaurant, Dish
from .forms import AddRestaurantForm, AddDishForm

# MAIN RESTAURANTS LIST
class RestaurantsView(View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        restaurant_ratings = {}
        for restaurant in restaurants:
            rating = Dish.objects.filter(restaurant=restaurant).aggregate(Avg('rating'))
            restaurant_ratings[restaurant.slug] = rating['rating__avg']

        context = {'restaurants': restaurants, 'restaurant_ratings': restaurant_ratings}
        return render(request, 'restaurants.html', context)

# ADD A RESTAURANT
class AddRestaurantView(View):
    def get(self, request):
        restaurant_from = AddRestaurantForm(prefix='restaurant_from')

        context = {'restaurant_from': restaurant_from}
        return render(request, 'addrestaurant.html', context)

    def post(self, request):
        restaurant_from = AddRestaurantForm(request.POST, prefix='restaurant_from')
        form_data = {}
        if restaurant_from.is_valid():
            for key, value in restaurant_from.cleaned_data.items():
                form_data[key] = value
            Restaurant.objects.create(**form_data)
        return redirect('/restaurants/')

# ADD A DISH
class AddDishView(View):
    def get(self, request):
        dish_from = AddDishForm(prefix='dish_from')

        context = {'dish_from': dish_from}
        return render(request, 'adddish.html', context)

    def post(self, request):
        dish_from = AddDishForm(request.POST, prefix='dish_from')
        form_data = {}
        if dish_from.is_valid():
            for key, value in dish_from.cleaned_data.items():
                form_data[key] = value
            Dish.objects.create(**form_data)
        return redirect('/restaurants/')


class SingleRestaurantDishesView(View):
    def get(self, request, **kwargs):
        restaurant_instance = Restaurant.objects.get(slug=kwargs['restaurant'])
        dishes = Dish.objects.filter(restaurant=restaurant_instance)
        context = {'restaurant': restaurant_instance, 'dishes': dishes}
        return render(request, 'dishes.html', context)


class SingleDishView(View):
    def get(self, request, **kwargs):
        dish = Dish.objects.get(slug="{}-{}".format(kwargs['restaurant'],kwargs['dish']))
        context = {'dish': dish}
        return render(request, 'singledish.html', context)

