import random

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
import os
import warnings
import json
import base64
from PIL import Image
import io
from datetime import datetime

from .models import Recipe
from .gr_dino import detect_ingredients
from .llama2 import generate_recipe, extract_recipe_info
from .sdxl import create_image, create_image_turbo

warnings.filterwarnings("ignore")
#
#
# config = {
#     "apiKey": "AIzaSyDbf7CxNP4Ce26wNilKl53ESlOZOgh-VXI",
#     "authDomain": "mms-project-65106.firebaseapp.com",
#     "projectId": "mms-project-65106",
#     "storageBucket": "mms-project-65106.appspot.com",
#     "messagingSenderId": "1034646575037",
#     "appId": "1:1034646575037:web:0750b961356ec5a3d164d4",
#     "measurementId": "G-KH24W3Y2R2"
# }
#
# firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()
#
# storage = firebase.storage()

CLASSES = "shrim . salmon . onions . tomatoes . potatoes . carrots . peas . beans . bell peppers . cabbage . broccoli . spinach . lettuce . garlic . rice . pasta . chicken . fish . eggs . milk . butter . cheese . salt . pepper . olive oil . sugar . flour . yeast . apples . oranges . bananas . strawberries . grapes . cherries . peaches . pears . peanuts . almonds . cashews . walnuts . yogurt . bread . chocolate . tea . coffee . vinegar . chili . bacon . sausage"


def convert_img(image_path):
    img = Image.open(image_path)
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return img_str

@api_view(['POST'])
def upload_images(request):
    images = request.FILES.getlist('images[]')
    total_ingredients = []

    if images:
        # Define the folder where you want to store the images
        upload_folder = 'data'

        # Create the folder if it doesn't exist
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

        detected_imgs = []

        # Iterate through the list of images and save them
        for image in images:
            # Generate a unique filename for each image (you can use other methods as well)
            image_name = image.name
            
            # Construct the path to save the image
            image_path = os.path.join(upload_folder, image_name)

            # Open the file and write the image content to it
            with open(image_path, 'wb') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            ingredients = detect_ingredients(image_path, CLASSES)
            total_ingredients += list(ingredients)

            img = convert_img(f"./output/vis/{image_name}")
            detected_imgs.append(img)

        detected_ingredients = list(set(total_ingredients))
        return Response({'ingredients': detected_ingredients, 'images': detected_imgs})
    else:
        return Response({'error': 'No images provided'}, status=400)


@api_view(['POST'])
def write_recipe(request):
    req_data = request.data
    ingredients = req_data["ingredients"]
    people = req_data["people"]
    duration = req_data["duration"]
    food = req_data["food"]
    raw_recipe = generate_recipe(ingredients=ingredients, num_people=people, cooking_time=duration, all_ingr=food)
    recipe_dict = extract_recipe_info(raw_recipe)

    # recipe_dict = {
    #     'Title': 'Quick and Healthy Quiche with a Fruit Twist',
    #     'QuantitiesRequired': {'olive oil': ' 2 tablespoons', 'tomatoes': ' 1 small (diced)', 'eggs': ' 4 large', 'apples': ' 1 small (sliced)', 'broccoli': ' 1/2 cup (chopped)'},
    #     'Description': 'A colorful and nutritious quiche, filled with a blend of vegetables, fruits, and eggs, creating a delicious meal for one.',
    #     'Instructions': '\n\n        1. Preheat your oven to 375°F (190°C).\n        2. In a large mixing bowl, whisk together the eggs, olive oil, diced tomatoes, and chopped broccoli. Season with salt and pepper.\n        3. Roll out your pie crust and place it into a 9-inch pie dish. Pour the egg mixture into the crust.\n        4. Arrange the sliced apples on top of the egg mixture.\n        5. Bake the quiche in the preheated oven for about 30-40 minutes or until the crust is golden brown and the eggs are set.\n        6. Remove from the oven and let cool for a few minutes before serving.\n\n        Enjoy your delicious and healthy Quick and Healthy Quiche with a Fruit Twist!\n'}

    recipe = Recipe()
    recipe.title = recipe_dict["Title"]
    recipe.ingredients = json.dumps(recipe_dict["QuantitiesRequired"])
    recipe.description = recipe_dict["Description"]
    recipe.instructions = recipe_dict["Instructions"]
    recipe.time_min = duration
    recipe.servings = people
    recipe.image_path = ""
    recipe.include_all = food
    recipe.pub_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    recipe.save()

    return Response({"recipe": recipe_dict, "id": recipe.id})


@api_view(['POST'])
def generate_image(request):
    req_data = request.data
    id_recipe = req_data["id"]
    recipe_instance = Recipe.objects.get(id=id_recipe)
    recipe = model_to_dict(recipe_instance)
    title = recipe["title"]
    description = recipe["description"]
    img = create_image_turbo(title, description)

    img_folder = "stable_images"
    # Create the folder if it doesn't exist
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    img.save(img_folder + str(id_recipe) + ".jpg")
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    recipe_instance.image_path = img_folder + str(id_recipe) + ".jpg"
    recipe_instance.save()

    return Response({"Image": img_str})


@api_view(['POST'])
def get_recipe_with_id(request):
    id_recipe = request.data["id"]
    recipe_instance = Recipe.objects.get(id=id_recipe)
    recipe = model_to_dict(recipe_instance)
    recipe["ingredients"] = json.loads(recipe["ingredients"])
    img_str = ""
    if recipe["image_path"] != "":
        img = Image.open(recipe["image_path"])
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return Response({"recipe": recipe, "image": img_str})


@api_view(['POST'])
def bookmark_recipe(request):
    id_recipe = request.data["id"]
    recipe_instance = Recipe.objects.get(id=id_recipe)
    recipe_instance.bookmarked = not recipe_instance.bookmarked
    recipe_instance.save()
    recipe = model_to_dict(recipe_instance)
    recipe["ingredients"] = json.loads(recipe["ingredients"])
    img_str = ""
    if recipe["image_path"] != "":
        img = Image.open(recipe["image_path"])
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return Response({"recipe": recipe, "image": img_str})


@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    recipes_list = []
    for recipe in recipes:
        recipe_dict = model_to_dict(recipe)
        recipe_dict["ingredients"] = json.loads(recipe_dict["ingredients"])
        if recipe_dict["image_path"] != "":
            img = Image.open(recipe_dict["image_path"])
            buffer = io.BytesIO()
            img.save(buffer, format="JPEG")
            img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
            recipe_dict["image"] = img_str
        recipes_list.append(recipe_dict)

    return Response({"recipes": recipes_list})
