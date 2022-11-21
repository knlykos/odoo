import tentaclio
import json

products_string = ""
setCategorias = set()
setSubCategorias = set()
productCategorias = {}

# with tentaclio.open("ftp://VHA1147:0Uh3XlZ6AKP3m39rrZKM@216.70.82.104/catalogo_xml/productos.json") as reader:
#     products_string = reader.read()

with open('productos.json') as reader:
    products_string = reader.read()

# reade
products = json.loads(products_string)
# print(products)

for i in range(0, len(products)):
    setCategorias.add(products[i]['idCategoria'])
    if products[i]['idCategoria'] in setCategorias:
        productCategorias[products[i]['idCategoria']] = products[i]

for idCategoria in setCategorias:
    print("product", productCategorias[idCategoria]['nombre'])
    # productCategorias[idCategoria] =
