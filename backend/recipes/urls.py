from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_images, name='upload_image'),
    path('write/', views.write_recipe, name='write_recipe'),
    path('image/', views.generate_image, name='image'),
    path('recipe/', views.get_recipe_with_id, name='recipe'),
    path('all/', views.get_all_recipes, name='all_recipes'),
    path('bookmark/', views.bookmark_recipe, name='bookmark'),
]
