from django.urls import path, include
from . import views

urlpatterns = [
path('', views.get_all_meals),
path('<int:id>/', views.get_category_meals),
]