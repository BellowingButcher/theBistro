from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import FullMenu

def get_all_meals(request):
    meals = list(FullMenu.objects.values('title', 'description', 'price', 'spicy_level', 'category__name', 'cuisine__name'))
    return JsonResponse({'Meals': meals})

def get_dinner_meals(request, id):
    meals = list(FullMenu.objects.filter(category__id=id).values('title', 'description', 'price', 'spicy_level', 'category__name', 'cuisine__name'))
    return JsonResponse({'Meals': meals})
# Create your views here.
