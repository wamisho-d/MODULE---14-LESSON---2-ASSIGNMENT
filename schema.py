# Task 1: Create a new file named schema.py and define the GraphQL schema to handle bakery inventory management.
# schema.py
import graphene

class Product(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    price = graphene.Float()
    quantity = graphene.Int()
    category = graphene.String()

class Query(graphene.ObjectType):
    products = graphene.List(Product)

    def resolve_products(self, info):
        # This data would typically come from a database
        return [
            Product(id=1, name="Croissant", price=2.5, quantity=30, category="Pastries"),
            Product(id=2, name="Baguette", price=3.0, quantity=20, category="Breads")
        ]

schema = graphene.Schema(query=Query)