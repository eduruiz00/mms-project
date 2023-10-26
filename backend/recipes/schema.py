import graphene
from recipes import queries


schema = graphene.Schema(query=queries.Query)
