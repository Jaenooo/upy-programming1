#13 copia el contenido de un archivo a otro
#1 - contener 3 lineas
#2 - luego copiar
#3 - imprimir

with open("registro.txt","w") as f:
    f.write("Linea 1\nlinea 2\nlinea 3\n")

with open("registro.txt","r") as origin, open("copia.txt","w") as destino:
    for linea in origen:
        destino.write(linea)
        
with open(