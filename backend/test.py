import requests

URL = 'http://localhost:5000/graphql'

def comprobar_query_productos():
    query = '''
    query {
        productos {
            id
            nombre
            stock
            disponible
        }
    }
    '''
    r = requests.post(URL, json={'query': query})
    assert r.status_code == 200
    resultado = r.json()
    assert 'data' in resultado
    assert 'productos' in resultado['data']
    assert isinstance(resultado['data']['productos'], list)
    print("La consulta de productos funciona bien")

def comprobar_mutacion_stock():
    mutation = '''
    mutation {
        modificarStock(id: 1, cantidad: -1) {
            producto {
                id
                stock
                disponible
            }
        }
    }
    '''
    r = requests.post(URL, json={'query': mutation})
    assert r.status_code == 200
    resultado = r.json()
    producto = resultado['data']['modificarStock']['producto']
    assert producto is not None
    assert isinstance(producto['stock'], int)
    assert isinstance(producto['disponible'], bool)
    print("La mutación de stock funciona bien")

if __name__ == "__main__":
    print("Comprobando el funcionamiento del back\n")
    comprobar_query_productos()
    comprobar_mutacion_stock()
    print("\nTodas las pruebas han pasado")