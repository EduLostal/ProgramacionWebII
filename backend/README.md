# Práctica Flask + GraphQL

Este repositorio tiene un backend sencillo para gestionar el inventario de una tienda online hecho mediante Flask y GraphQL

## Cómo ejecutar el proyecto?

### Crea el entorno (en mi caso utilizare conda por costumbre):

conda create -n inventario-backend python=3.11
conda activate inventario-backend

### Instala las dependencias en el entorno elegido

pip install flask flask-graphql graphene

### inicia el servidor a través de app.py

python app.py

### La parte del back puede probarse a través de "http://localhost:5000/graphql" utilizando algunas querys (dejo un par de ejemplo)

query {
  productos {
    id
    nombre
    precio
    stock
    disponible
  }
}

o

mutation {
  modificarStock(id: 1, cantidad: -1) {
    producto {
      nombre
      stock
      disponible
    }
  }
}

### Cada reincio del servidor vuelve las cantidades a su estado original



