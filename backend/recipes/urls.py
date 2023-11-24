from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_images, name='upload_image'),
    path('write/', views.write_recipe, name='write_recipe'),
    path('image/', views.generate_image, name='image')
]
