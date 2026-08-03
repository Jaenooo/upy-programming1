#18 solo leeremos los pares y los que no sean los pasaremos a otra carpeta

with open("origen.txt", "w") as f:
    f.write("3\n8\n9\n3\n6\n7\n5\n1\n2\n")
    
with open("origen.txt", "r") as entrada, open("destino.txt", "w") as salida:
    for linea in entrada:
        n = int(linea)
        if n % 2 == 0:
            salida.write(str(n) + "\n")
    