import graphene
from graphene_django import DjangoObjectType
from recipes import models


class IngredientType(DjangoObjectType):
    class Meta:
        model = models.Ingredient