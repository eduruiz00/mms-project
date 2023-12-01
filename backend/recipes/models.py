from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField(max_length=10000)
    description = models.TextField(max_length=1000)
    instructions = models.TextField(max_length=10000)
    time_min = models.CharField(max_length=10)
    servings = models.CharField(max_length=10)
    image_path = models.CharField(max_length=600)
    include_all = models.CharField(max_length=15)
    bookmarked = models.BooleanField(default=False)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title


class IngredientRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)

    def __str__(self):
        return self.amount


class PictureItems(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

