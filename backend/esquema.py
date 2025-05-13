import graphene
from productos import productos

# Tipo Producto
class Producto(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

# Query para obtener todos los productos
class Query(graphene.ObjectType):
    productos = graphene.List(Producto)

    def resolve_productos(self, info):
        return productos

# Mutación para cambiar stock
class ModificarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(lambda: Producto)

    def mutate(self, info, id, cantidad):
        # Buscamos el producto
        for p in productos:
            if p["id"] == id:
                p["stock"] += cantidad
                # Asegurarse de que no quede stock negativo
                if p["stock"] < 0:
                    p["stock"] = 0
                # Actualizar disponibilidad
                if p["stock"] == 0:
                    p["disponible"] = False
                else:
                    p["disponible"] = True
                return ModificarStock(producto=p)
        raise Exception("Producto no encontrado")

# Definimos esquema
class Mutation(graphene.ObjectType):
    modificar_stock = ModificarStock.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
