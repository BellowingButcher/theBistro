from django.urls import path, include
from . import views

urlpatterns = [
path('menus/', views.get_all_meals),
path('menus/<int:id>/', views.get_category_meals),
path('menus/<str:name>/', views.get_cuisine_meals),
]
# ===============================================================================
# failed pathways
# I am trying to pull the url that the front end would use to access the cuisine filtered portion of the database.  
# Found it! use str instead of int inside the pathway <str:name>  

# urlpatterns = [
# path('menus/', views.get_all_meals),
# path('menus/<int:id>/', views.get_category_meals),
# path('menus/<int:id>/<int:name>/', views.get_cuisine_meals),
# ]

# urlpatterns = [
# path('menus/', views.get_all_meals),
# path('menus/<int:id>/', views.get_category_meals),
# path('menus/<int:name>/', views.get_cuisine_meals),
# ]