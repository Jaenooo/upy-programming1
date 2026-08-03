#17 lista(producto y precio)
#Encabezado
#Producto precio
#lapiz 8

productos = [("Lapiz", 8),("Borrador", 3),("Tajador", 5),("Cuaderno", 10)]

with open ("productos.txt","w") as f:
    f.write("producto precio\n")
    for nombre, precio in productos:
        f.write(nombre + " " + str(precio) + "\n")