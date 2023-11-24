from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import warnings
import json
import base64
from PIL import Image
import io

from .gr_dino import detect_ingredients
from .llama2 import generate_recipe, extract_recipe_info
from .sdxl import create_image

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

CLASSES = "shrims . salmon . onions . tomatoes . potatoes . carrots . peas . beans . bell peppers . cabbage . broccoli . spinach . lettuce . garlic . mushrooms . rice . pasta . chicken . beef . fish . eggs . milk . butter . cheese . salt . pepper . olive oil . sugar . flour . yeast . apples . oranges . bananas . strawberries . grapes . cherries . peaches . pears . peanuts . almonds . cashews . walnuts . yogurt . bread . chocolate . tea . coffee . vinegar . chili . bacon . sausage"


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

        detected_ingredients = list(set(total_ingredients))
        print(detected_ingredients)
        return Response({'ingredients': detected_ingredients})
    else:
        return Response({'error': 'No images provided'}, status=400)


@api_view(['POST'])
def write_recipe(request):
    req_data = request.data
    print(req_data["ingredients"])
    print(req_data["people"])
    print(req_data["duration"])
    print(req_data["food"])
    raw_recipe = generate_recipe(ingredients="potatoes, chicken", num_people=2, cooking_time=45, all_ingr=True, model=True)
    recipe_dict = extract_recipe_info(raw_recipe)
    title = recipe_dict["Title"]
    description = recipe_dict["Description"]
    img = create_image(title, description)
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return Response({"recipe": recipe_dict, "Image": img_str})