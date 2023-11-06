# from sdxl import create_image
# from llama2 import generate_recipe
from gr_dino import detect_ingredients
# import re
import warnings

warnings.filterwarnings("ignore")

classes = "shrims . salmon . onions . tomatoes . potatoes . carrots . peas . beans . bell peppers . cabbage . broccoli . spinach . lettuce . garlic . mushrooms . rice . pasta . chicken . beef . fish . eggs . milk . butter . cheese . salt . pepper . olive oil . sugar . flour . yeast . apples . oranges . bananas . strawberries . grapes . cherries . peaches . pears . peanuts . almonds . cashews . walnuts . yogurt . bread . chocolate . tea . coffee . vinegar . chili . bacon . sausage"

img = "data/prova.jpg"

ingredients = detect_ingredients(img, classes)
print(ingredients)
#
# # Generate a recipe based on list of ingredients
# full_recipe = generate_recipe(ingredients, 4, 90)
#
# def extract_recipe_info(input_string):
#     assistant_info = {}
#     parts = re.split("### Assistant:", input_string)[-1]
#     title = re.search(r'Title: "([^"]+)"', parts).group(1)
#     assistant_info['Title'] = title
#
#     # Extract Quantities Required
#     quantities_match = re.search(r'Quantities Required:\n(([^\n]+:[^\n]+\n)+)', parts)
#     if quantities_match:
#         quantities_section = quantities_match.group(1)
#         quantities = {}
#         quantity_lines = quantities_section.strip().split('\n')
#         for line in quantity_lines:
#             line = re.sub('"',"", line)
#             ingredient, amount = line.split(':')
#             quantities[ingredient.strip()] = amount
#         assistant_info['Quantities Required'] = quantities
#
#     # Extract Description
#     description_match = re.search(r'Description: "([^"]+)"', parts)
#     if description_match:
#         assistant_info['Description'] = description_match.group(1)
#     else:
#         description_match = re.search(r'Description: ([^"]+)', parts)
#         if description_match:
#             assistant_info['Description'] = description_match.group(1)
#
#     # Extract Instructions
#     instructions_match = re.search(r'Instructions:(.*)<\/s>', parts, re.DOTALL)
#     if instructions_match:
#         assistant_info['Instructions'] = instructions_match.group(1)
#
#     return assistant_info
#
# recipe_info = extract_recipe_info(full_recipe)
# if recipe_info:
#     print("\n-------------------------------------------------\n")
#     print("Dish Name:", recipe_info["Title"], "\n")
#     print("Ingredient Quantities:\n",
#           '\n'.join([f"{key}: {value}" for key, value in recipe_info["Quantities Required"].items()]), "\n")
#     print("Dish Description:", recipe_info["Description"], "\n")
#     print("Cooking Steps:\n", recipe_info["Instructions"], "\n")
# else:
#     print("Assistant section not found in the input.")
#
#
# dish_image = create_image(recipe_info["Title"], recipe_info["Description"])
# dish_image.save("output/output.jpg")