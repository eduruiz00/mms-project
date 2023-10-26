import graphene
from recipes import models
from recipes import types


# The Query class
class Query(graphene.ObjectType):
    ingredient = graphene.Field(types.IngredientType)

    def resolve_ingredient(root, info):
        return (
            models.Ingredient.objects.first()
        )
