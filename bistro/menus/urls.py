from django.urls import path, include
from . import views

urlpatterns = [
path('', views.get_all_meals),
path('Dinner/<int:id>', views.get_dinner_meals),
]