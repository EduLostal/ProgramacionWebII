import graphene
from productos import productos

# Definimos el modelo de datos para un producto
class Producto(graphene.ObjectType):
    id = graphene.Int()
    nombre = graphene.String()
    precio = graphene.Float()
    stock = graphene.Int()
    disponible = graphene.Boolean()

# Consulta principal que devuelve la lista de productos
class Query(graphene.ObjectType):
    productos = graphene.List(Producto)

    def resolve_productos(self, info):
        return productos

# Mutación para modificar el stock de un producto
class ModificarStock(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        cantidad = graphene.Int(required=True)

    producto = graphene.Field(lambda: Producto)

    def mutate(self, info, id, cantidad):
        # Buscar el producto en la lista
        for p in productos:
            if p["id"] == id:
                p["stock"] += cantidad
                # El stock no puede ser negativo
                if p["stock"] < 0:
                    p["stock"] = 0
                # Actualizar la disponibilidad en función del stock
                p["disponible"] = p["stock"] > 0
                return ModificarStock(producto=p)
        
        # Si no se encuentra el producto, devolver None
        return ModificarStock(producto=None)

# Definimos la clase que agrupa las mutaciones disponibles
class Mutation(graphene.ObjectType):
    modificar_stock = ModificarStock.Field()

# Creamos el esquema GraphQL combinando consultas y mutaciones
schema = graphene.Schema(query=Query, mutation=Mutation)
