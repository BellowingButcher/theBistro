from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from django.shortcuts import render
from menus.serializers import MenusSerializer, GroupSerializer
from .models import FullMenu
# from django.http import HttpResponse, JsonResponse



class MenusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = FullMenu.objects.all()
    serializer_class = MenusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]










# def get_all_meals(request):
#     meals = list(FullMenu.objects.values('title', 'description', 'price', 'spicy_level', 'category__name', 'cuisine__name'))
#     return JsonResponse({'Meals': meals})

# def get_category_meals(request, id):
#     meals = list(FullMenu.objects.filter(category__id=id).values('title', 'description', 'price', 'spicy_level', 'category__name', 'cuisine__name'))
#     return JsonResponse({'Meals': meals})

# def get_cuisine_meals(request, name):
#     meals = list(FullMenu.objects.filter(cuisine__name=name).values('title', 'description', 'price', 'spicy_level', 'category__name', 'cuisine__name'))
#     return JsonResponse({'Meals': meals})
# # Create your views here.
