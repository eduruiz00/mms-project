from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    instructions = models.TextField(max_length=2000)
    time_min = models.IntegerField(default=0)
    servings = models.IntegerField(default=0)
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

