from django.shortcuts import render
# import pyrebase
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
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


@csrf_exempt  # Use this decorator to disable CSRF protection for this view@csrf_exempt  # Use this decorator to disable CSRF protection for this view
def upload_images(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images[]')

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

            return JsonResponse({'message': 'Images uploaded successfully'})
        else:
            return JsonResponse({'error': 'No images provided'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
