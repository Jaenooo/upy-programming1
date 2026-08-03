#12
#Agregar la palabra "cierre de sesion". y mostrar

with open("registro.txt","w") as f:
    f.write("Inicio de sesion\n ")
    
with open("registro.txt","w") as F:
    F.write("cierre de sesion")

with open("registro.txt", "r") as f:
    print(f.read())