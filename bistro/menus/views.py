from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import FullMenu

def get_all_meals(request):
    meals = list(FullMenu.objects.values())
    return JsonResponse({'Meals': meals})

# Create your views here.
